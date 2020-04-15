import os

instructions = open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3])).read().split('\n')

order = []

for i in instructions:
    order.append([i.split('Step ')[1][0], i.split('step ')[1][0]])

goals = set(x[0] for x in order).union(set(x[1] for x in order))

goals = sorted([x for x in goals])

steps = {key[1]: set(step[0] for step in order if step[1] is key[1]) for key in order}

done = set()

steporder = ""

while len(done) is not len(goals):
    for key in goals:
        if key not in done:
            if key in steps:
                if steps[key].issubset(done):
                    done.add(key)
                    steporder += key
                    break
            else:
                done.add(key)
                steporder += key
                break

print(steporder)

done = set()

workers = [['free', 0], ['free', 0], ['free', 0], ['free', 0], ['free', 0]]

time = 0
while len(done) is not len(goals) + 1:
    for key in goals:
        if key not in done and key not in [worker[0] for worker in workers]:
            if key in steps:
                if steps[key].issubset(done) and len(
                        [index for (index, x) in enumerate(workers) if x[0] == 'free']) > 0:
                    workers[[index for (index, x) in enumerate(workers) if x[0] == 'free'][0]] = [key,60 + ord(key) - 63]
            else:
                try:
                    workers[[index for (index, x) in enumerate(workers) if x[0] == 'free'][0]] = [key,60 + ord(key) - 63]
                except IndexError:
                    pass
    for (index, worker) in enumerate(workers):
        if worker[1] == 0 or worker[1] == 1:
            done.add(worker[0])
            workers[index] = ['free', 0]
            for key in goals:
                if key not in done and key not in [worker[0] for worker in workers]:
                    if key in steps:
                        try:
                            if steps[key].issubset(done):
                                workers[[index for (index, x) in enumerate(workers) if x[0] == 'free'][0]] = [key, 60 + ord(key) - 64]
                                break
                        except IndexError:
                            pass

                    else:
                        try:
                            workers[[index for (index, x) in enumerate(workers) if x[0] == 'free'][0]] = [key, 60 + ord(key) - 64]
                            break
                        except IndexError:
                            pass
        else:
            workers[index] = [worker[0], worker[1] - 1]
    time += 1
print(time - 1)
