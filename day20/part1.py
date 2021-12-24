def readfile(filename):
    with open(filename) as f:
        lines = f.readlines()
        algo = lines[0].strip()
        img = []
        for line in lines[2:]:
            img.append(list(line.strip()))
        return algo, img


def expand(img):
    img = list(map(lambda row: list('..') + row + list('..'), img))
    empty_row = list('.' * len(img[0]))
    img.insert(0, empty_row.copy())
    img.insert(0, empty_row.copy())
    img.append(empty_row.copy())
    img.append(empty_row.copy())
    return img


def get_window_value(img, x, y):
    pix_pos = [
            (x-1, y-1),
            (x, y-1),
            (x+1, y-1),
            (x-1, y),
            (x, y),
            (x+1, y),
            (x-1, y+1),
            (x, y+1),
            (x+1, y+1),
        ]
    b = ''
    rowlen = len(img[0])
    collen = len(img)
    for pos in pix_pos:
        x, y = pos
        if 0 <= x < rowlen and 0 <= y < collen:
            if img[y][x] == '#':
                b += '1'
            else:
                b += '0'
        else:
            b += '0'
    return int(b, 2)


def apply_step(img, algo):
    new_row = list('.' * (len(img[0]) + 4))
    res = []
    for _ in range(len(img)+4):
        res.append(new_row.copy())

    for y in range(len(res) - 2):
        for x in range(len(res[0]) - 2):
#            y += 1
#            x += 1


            print(get_window_value(img, y-1, x-1))
            print(y, x, len(res), len(res[0]))
            
            res[y+1][x+1] = algo[get_window_value(img, y, x)]


#    img = expand(img)
#    print('EXPANDED: ')
#    for row in img:
#        print(''.join(row))
#    print()

    # TODO:Find a pixel that differs in the example and my output and debug based on that

#    for y, row in enumerate(img[1:-1]):
#        for x, val in enumerate(row[1:-1]):
#            res[y+1][x+1] = algo[get_window_value(img, y+1, x+1)]
#
    return res


# algo, img = readfile('input1')
algo, img = readfile('testinput')
# algo, img = readfile('testinput1')
# algo, img = readfile('testinput2')


for row in img:
    print(''.join(row))


img = apply_step(img, algo)

for row in img:
 print(''.join(row))

img = apply_step(img, algo)

s = 0
for row in img:
    for val in row:
        if val == '#':
            s += 1

for row in img:
    print(''.join(row))

print(s)

