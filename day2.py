import os

instructions = open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3])).read().split()

ids = [{y: x.count(y) for y in x} for x in instructions]

twos = 0
threes = 0

for id in ids:
    if 2 in [id[key] for key in id]:
        twos += 1
    if 3 in [id[key] for key in id]:
        threes += 1
print(twos * threes)

runs = 0
search = True

while search:
    newlist = [instructions[runs]] + instructions[:runs] + instructions[runs:]

    for x in newlist[1:]:
        diff = []
        for (index, y) in enumerate(x):
            if y != newlist[0][index]:
                diff.append(index)
        if len(diff) == 1:
            print(x + '\n' + newlist[0])
            search = False
    runs += 1
