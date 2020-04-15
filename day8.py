import os, functools, sys

sys.setrecursionlimit(10000)

instructions = open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3])).read().split('\n')[0]

instructions = [int(i) for i in instructions.split()]


def tree(list):
    if list == []:
        return []
    ccount = list[0]
    mcount = list[1]
    if ccount == 0:
        return list[2:2 + mcount] + tree(list[2 + mcount:])
    if ccount == 1 and list[2] == 0:
        return list[4: 4 + list[3]] + list[4 + list[3]: 4 + list[3] + mcount] + tree(list[4 + list[3] + mcount:])
    else:
        return list[len(list) - mcount:] + tree(list[2:len(list) - mcount])


print(functools.reduce(lambda x, y: x + y, tree(instructions)))
