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


hmap = readfile('input1')

#lowpoints = []
s = 0
for y, row in enumerate(hmap):
    for x, val in enumerate(row):
        if is_lowpoint(hmap, x, y):
            s += (hmap[y][x] + 1)


print(s)
