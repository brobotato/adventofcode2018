import os

instructions = open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3])).read().split()

vals = set()
sums = dict()
loops = 0
run = True

for x in range(1, len(instructions) + 1):
    sums[x] = eval('0' + ''.join(instructions[:x]))
print(sums[len(instructions)])

while run:
    for x in range(1, len(instructions) + 1):
        sum = loops * sums[len(instructions)] + sums[x]
        if sum in vals:
            print(sum)
            run = False
            break
        else:
            vals.add(sum)
    loops += 1
