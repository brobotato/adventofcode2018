import os

instructions = open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3])).read().split('\n')

fabric = [[None for y in range(1, 1001)] for x in range(1, 1001)]
overlap = [[None for y in range(1, 1001)] for x in range(1, 1001)]
overlappers = set()
ids = [x for x in range(1, len(instructions) + 1)]

for x in instructions:
    id = x.split('@ ')[0][1:]
    claim = x.split('@ ')[1].split(': ')
    coords = claim[0].split(',')
    x, y = int(coords[0]), int(coords[1])
    dims = claim[1].split('x')
    width, height = int(dims[0]), int(dims[1])
    for unit_x in range(width):
        for unit_y in range(height):
            if fabric[x + unit_x][y + unit_y] is None:
                fabric[x + unit_x][y + unit_y] = 1
                overlap[x + unit_x][y + unit_y] = int(id)
            else:
                fabric[x + unit_x][y + unit_y] += 1
                overlappers.add(overlap[x + unit_x][y + unit_y])
                overlappers.add(int(id))

total = 0
for row in fabric:
    for column in row:
        if not column is None:
            if column > 1:
                total += 1

print(total)
print([y for y in ids if y not in overlappers][0])
