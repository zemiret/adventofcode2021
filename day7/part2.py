def readfile(filename):
    with open(filename) as f:
        return list(map(lambda x: int(x), f.readline().split(',')))


def cost(crab, pos):
    cp = abs(crab - pos)
    return int(cp * (cp + 1)/2)


def total(crabs, pos):
    return sum(map(lambda x: cost(x, pos), crabs))


crabs = readfile('input1')

maxp = max(crabs)
minp = min(crabs)

costs = []
for p in range(minp, maxp):
    costs.append(total(crabs, p))

val, idx = min((val, idx) for (idx, val) in enumerate(costs))

print(val)
