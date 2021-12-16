import math

def readfile(filename):
    with open(filename) as f:
        return list(map(lambda s: [int(x) for x in s.strip()], f.readlines()))


# cave = readfile('testinput')
cave = readfile('input1')
cavew = len(cave[0])
caveh = len(cave)


i = 0

def relax(pos, cave, pathrisk):
    # for now I assume you can only walk down and right 
    x, y = pos
    risk_at_pos = cave[y][x]

    x_left, y_left = x-1, y
    if x_left >= 0:
        risk_from_left = pathrisk[y_left][x_left] + risk_at_pos
        if risk_from_left < pathrisk[y][x]:
            pathrisk[y][x] = risk_from_left

    x_top, y_top = x, y-1
    if y_top >= 0:
        risk_from_top = pathrisk[y_top][x_top] + risk_at_pos
        if risk_from_top < pathrisk[y][x]:
            pathrisk[y][x] = risk_from_top


def walk(cave, pathrisk):
    for i in range(1, cavew):
        # check horizontal line)
        for x in range(i+1):
            relax((x, i), cave, pathrisk)
        # check vertical line)
        for y in range(i+1):
            relax((i, y), cave, pathrisk)


pathrisk = [[math.inf for _ in range(cavew)] for _ in  range(caveh)] 
pathrisk[0][0] = 0

print(cavew, caveh)

walk(cave, pathrisk)

for row in pathrisk:
    print(row)


print(pathrisk[caveh-1][cavew-1])
