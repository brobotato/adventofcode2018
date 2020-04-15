import os, functools

instructions = open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3])).read().split('\n')

instructions = [eval('[' + x + ']') for x in instructions]

grid = [[None for x in range(400)] for y in range(400)]

ids = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

starters = dict()

for (index, x) in enumerate(instructions):
    grid[x[1]][x[0]] = ids[index]
    starters[ids[index]] = (x[1], x[0])


for (r_i, row) in enumerate(grid):
    for (c_i, column) in enumerate(row):
        if column is None:
            distances = {key: abs(starters[key][0] - r_i) + abs(starters[key][1] - c_i) for key in starters}
            vals = sorted([[distances[key], key] for key in distances])
            if vals[0][0] == vals[1][0]:
                grid[r_i][c_i] = '.'
            else:
                grid[r_i][c_i] = vals[0][1]

infinite = set()

for x in range(400):
    infinite.add(grid[0][x])
    infinite.add(grid[399][x])
    infinite.add(grid[x][0])
    infinite.add(grid[x][399])

total = dict()

for dists in [{k: g.count(k) for k in g if k not in infinite} for g in grid]:
    for key in dists:
        if key in total:
            total[key] += dists[key]
        else:
            total[key] = dists[key]

print(sorted([total[key] for key in total], reverse=True)[0])


def total_dist(x, y):
    total = 0
    for key in starters:
        total += abs(starters[key][0] - x) + abs(starters[key][1] - y)
    return total


area = 0

for x in range(400):
    for y in range(400):
        if total_dist(x, y) < 10000:
            area += 1

print(area)
