from collections import namedtuple
from itertools import chain
import math

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x}, {self.y})'

def readinput(filename):
    lines = []

    with open(filename) as f:
        inputlines = f.readlines()
        for line in inputlines:
            start_point, end_point = list(map(lambda x: P(int(x[0]), int(x[1])), map(lambda p: p.strip().split(','), line.split('->'))))
            lines.append((start_point, end_point))

    return lines


def min_max(lines):
    min_p = P(math.inf, math.inf)
    max_p = P(-math.inf, -math.inf)

    for line in lines:
        for point in line:
            if point.x < min_p.x:
                min_p.x = point.x
            if point.y < min_p.y:
                min_p.y = point.y
            if point.x > max_p.x:
                max_p.x = point.x
            if point.y > max_p.y:
                max_p.y = point.y

    return (min_p, max_p)


def mark(matrix, line):
    p1, p2 = line[0], line[1]

    x_inc = (p2.x > p1.x and 1) or (p2.x < p1.x and -1) or 0
    y_inc = (p2.y > p1.y and 1) or (p2.y < p1.y and -1) or 0

    # only hor and vert lines - UNCOMMENT FOR 1st PART
#    if x_inc != 0 and y_inc != 0:
#        return

    x, y = p1.x, p1.y

    while x != p2.x or y != p2.y:
        matrix[y][x] += 1
        x += x_inc
        y += y_inc

    # mark last point
    matrix[y][x] += 1



lines = readinput('input1')
min_p, max_p = min_max(lines)

matrix = []
row = [0] * (max_p.x + 1)
for y in range(max_p.y+1):
    matrix.append(row.copy())


for line in lines:
    mark(matrix, line)

print(len(list(filter(lambda x: x > 1, chain.from_iterable(matrix)))))

