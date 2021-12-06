def readfile(filename):
    with open(filename) as f:
        return list(map(lambda x: int(x), f.readline().split(',')))


fishes = readfile('input1')

def pass_day(fishes):
    new_fishes = []

    for i, fish in enumerate(fishes):
        if fish == 0:
            fishes[i] = 6
            new_fishes.append(8)
        else:
            fishes[i] -= 1

    return fishes + new_fishes

for day in range(80):
    fishes = pass_day(fishes)

print(len(fishes))
