def readfile(filename):
    dots, instructions = [], []
    reading_inst = False

    with open(filename) as f:
        for line in map(lambda s: s.strip(), f.readlines()):
            if line == "":
                reading_inst = True
                continue

            if reading_inst:
                foldline = line.split()[-1]
                axis, cord = foldline.split('=')
                instructions.append((axis, int(cord)))
            else:
                dots.append([int(x) for x in line.split(',')])

    return dots, instructions

dots, instructions = readfile('input1')

for inst in instructions:
    fold_cord = inst[1]
    new_dots = []
    for dot in dots:
        x, y = dot
        if inst[0] == 'y':
            if y > fold_cord:
                y = y - (y - fold_cord)*2
        if inst[0] == 'x':
            if x > fold_cord:
                x = x - (x - fold_cord)*2

        if [x, y] not in new_dots:
            new_dots.append([x, y])

    dots = new_dots



matrix = []
for i in range(10):
    matrix.append((['.'] * 50).copy())

for dot in dots:
    matrix[dot[1]][dot[0]] = '❚'

for row in matrix:
    print(''.join(row))
print()

