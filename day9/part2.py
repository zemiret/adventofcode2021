import math

def readfile(filename):
    with open(filename) as f:
        return [[int(y) for y in x.strip()] for x in f.readlines()]


def up(hmap, x, y):
    if y == 0:
        return math.inf
    return hmap[y-1][x]

def down(hmap, x, y):
    if y == len(hmap) - 1:
        return math.inf
    return hmap[y+1][x]

def left(hmap, x, y):
    if x == 0:
        return math.inf
    return hmap[y][x-1]

def right(hmap, x, y):
    if x == len(hmap) - 1:
        return math.inf
    return hmap[y][x+1]


def is_lowpoint(hmap, x, y):
    val = hmap[y][x]
    return val < up(hmap,x,y) and\
            val < down(hmap,x,y) and\
            val < left(hmap,x,y) and\
            val < right(hmap,x,y)


def expand_basin(hmap, point, basin):
    # stop conditions - edge of the map or checked already
    x, y = point
    if x == -1 or x == len(hmap[0]):
        return set() 
    if y == -1 or y == len(hmap):
        return set()
    if point in basin:
        return set() 
    if hmap[y][x] == 9:
        return set()

    up = (x, y-1)
    down = (x, y+1)
    left = (x-1, y)
    right = (x+1, y)

    basin |= {point}
    basin |= expand_basin(hmap, up, basin) 
    basin |= expand_basin(hmap, down, basin) 
    basin |= expand_basin(hmap, left, basin) 
    basin |= expand_basin(hmap, right, basin) 

    return basin


hmap = readfile('input1')
# hmap = readfile('testinput')

lowpoints = []
s = 0
for y, row in enumerate(hmap):
    for x, val in enumerate(row):
        if is_lowpoint(hmap, x, y):
            lowpoints.append((x,y))


basins = []

for point in lowpoints:
    basin = expand_basin(hmap, point, set())
    basins.append(basin)


biggest = sorted(map(len, basins), key=lambda x: -x)[0:3]
print(biggest[0] * biggest[1] * biggest[2])

