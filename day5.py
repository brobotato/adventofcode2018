import os, copy

instructions = open('./input/{0}.txt'.format(os.path.basename(__file__)[:-3])).read().split('\n')[0]
run = True

lower = [x + x.upper() for x in 'qwertyuiopasdfghjklzxcvbnm']
upper = [x.upper() + x for x in 'qwertyuiopasdfghjklzxcvbnm']

l2 = instructions
run = True
while run:
    l1 = copy.copy(l2)

    for l in lower:
        l1 = l1.replace(l, '')
    for u in upper:
        l1 = l1.replace(u, '')

    if l1 is l2:
        print(len(l1))
        run = False

    else:
        l2 = l1

minimum = 100000

for x in "qwertyuiopasdfghjklzxcvbnm":
    l2 = instructions.replace(x, '')
    l2 = l2.replace(x.upper(), '')

    run = True
    while run:
        l1 = copy.copy(l2)

        for l in lower:
            l1 = l1.replace(l, '')
        for u in upper:
            l1 = l1.replace(u, '')

        if l1 is l2:
            minimum = min(minimum, len(l1))
            run = False

        else:
            l2 = l1

print(minimum)
