import math
from itertools import combinations


def readfile(filename):
    lines = []
    with open(filename) as f:
        for line in f.readlines():
            lines.append(parse_line(line))
    return lines




# Maybe it'd be beter to have heterogenous list? Like
# ['[', 2, '[', 4, 5, ']', ']']

# [1,2] + [3,4]
# ['[', 1, 2, ']']
# ['[', '[', 1, 2, ']', '[', 3, 4, ']', ']']

def parse_line(line):
    num = []
    for c in line.strip():
        if c in ['[', ']']:
            num.append(c)
        elif c != ',':
            num.append(int(c))
    return num



def nums_from_pair(pair):
    return list(map(lambda n: int(n), pair[1:-1].split(',')))


def explode(line):
    open_pairs = 0
    explode_pos = 0

    for i, c in enumerate(line):
        if c == '[':
            open_pairs += 1
        if c == ']':
            open_pairs -= 1

        if open_pairs == 5: # 5 cause nested inside 4 pairs is 5th
            explode_pos = i # Is it alwyas true? Or maybe this can be not a regular pair?
            break

    if explode_pos == 0:
        return line, False


    line_before = line[:explode_pos]
    line_after = line[explode_pos+4:]
    n1, n2 = line[explode_pos+1], line[explode_pos+2]

    i = len(line_before)-1
    while i >= 0:
        if isinstance(line_before[i], int):
            line_before[i] += n1
            break
        i -= 1

    i = 0
    while i < len(line_after):
        if isinstance(line_after[i], int):
            line_after[i] += n2
            break
        i += 1

    
    line = line_before + [0] + line_after
    return line, True


def split(line):
    split_pos = 0
    for i, c in enumerate(line):
        if isinstance(c, int) and c >= 10:
            split_pos = i
            break

    if split_pos == 0:
        return line, False

    n = line[split_pos]
    before_split = line[:split_pos]
    after_split = line[split_pos+1:]

    return before_split + ['[', math.floor(n/2), math.ceil(n/2), ']'] + after_split, True


def reduce(line):
    while True:
        line, exploded = explode(line)
        if exploded:
            continue

        line, splitted = split(line)
        if splitted:
            continue

        break
    return line


def add(n1, n2):
    line = ['['] + n1 + n2 + [']']
    return line


def magnitude(line):
    mag = line.copy()
    # find "small" pair, replace it with its magnitude, make new line until we're at last pair

    while len(mag) > 4:
        i = 0
        while mag[i] != '[' or mag[i+3] != ']':
            i += 1

        before_pair = mag[:i]
        after_pair = mag[i+4:]
        m = mag[i+1] * 3 + mag[i+2] * 2
        mag = before_pair + [m] + after_pair

    m = mag[1] * 3 + mag[2] * 2
    return m



def print_line(line):
    for c in line:
        print(c, end=' ')
    print()


lines = readfile('input1')

max_mag = -math.inf
for pair in combinations(lines, 2):
    s = add(pair[0], pair[1])
    s = reduce(s)
    mag = magnitude(s)
    if mag > max_mag:
        max_mag = mag

    s = add(pair[1], pair[0])
    s = reduce(s)
    mag = magnitude(s)
    if mag > max_mag:
        max_mag = mag

print(max_mag)

