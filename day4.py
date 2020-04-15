import os, operator

instructions = open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3])).read().split('\n')

data = sorted([[x.split('] ')[0][1:], x.split('] ')[1]] for x in instructions])

hours = dict()

for (index, x) in enumerate(data):
    if "#" in x[1]:
        current_guard = x[1][x[1].index('#'):x[1].index('#') + x[1][x[1].index('#'):].index(' ')]
        if current_guard not in hours:
            hours[current_guard] = 0
    if "falls asleep" in x[1]:
        hours[current_guard] += int(
            data[index + 1][0][data[index + 1][0].index(':') + 1:data[index + 1][0].index(':') + 1 + 2]) \
                                - int(x[0][x[0].index(':') + 1:x[0].index(':') + 1 + 2])

time = {y: {x: 0 for x in range(60)} for y in hours}

for (index, x) in enumerate(data):
    if "#" in x[1]:
        current_guard = x[1][x[1].index('#'):x[1].index('#') + x[1][x[1].index('#'):].index(' ')]
    if "falls asleep" in x[1]:
        for y in range(
                int(data[index + 1][0][data[index + 1][0].index(':') + 1:data[index + 1][0].index(':') + 1 + 2]) - int(
                    x[0][x[0].index(':') + 1:x[0].index(':') + 1 + 2])):
            time[current_guard][int(x[0][x[0].index(':') + 1:x[0].index(':') + 1 + 2]) + y] += 1

max = 0
maxind = 0
guard = "hey"
for x in time:
    for y in time[x]:
        if time[x][y] > max:
            max = time[x][y]
            maxind = y
            guard = x

mostsleep = sorted(hours.items(), reverse=True, key=operator.itemgetter(1))[0][0]

print(mostsleep, sorted(time[mostsleep].items(), reverse=True, key=operator.itemgetter(1))[0][0])

print(guard, maxind)
