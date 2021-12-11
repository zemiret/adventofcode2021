def readfile(filename):
    with open(filename) as f:
        return list(map(lambda s: [int(x) for x in s.strip()], f.readlines()))

grid = readfile('input1')

gridh = len(grid)
gridw = len(grid[0])

def in_bounds(p):
    x, y = p
    return 0 <= x < gridw and 0 <= y < gridh

def step(grid):
    flashes = 0
    flash_stack = []
    already_flashed = set()

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            grid[y][x] += 1
    
    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            if val > 9:
                flash_stack.append((x, y))
                already_flashed |= {(x, y)}

    rowlen = len(grid[0])

    while len(flash_stack) > 0:
        x, y = flash_stack.pop()

        flashes += 1

        upleft = (x-1, y-1)
        up = (x, y-1)
        upright = (x+1, y-1)
        right = (x+1, y)
        downright = (x+1, y+1)
        down = (x, y+1)
        downleft = (x-1, y+1)
        left = (x-1, y)

        for check_p in [upleft, up, upright, right, downright, down, downleft, left]:
            if in_bounds(check_p):
                cx, cy = check_p
                grid[cy][cx] += 1
                if grid[cy][cx] > 9 and check_p not in already_flashed:
                    flash_stack.append(check_p)
                    already_flashed |= {(cx, cy)}


    for x, y in already_flashed:
        grid[y][x] = 0

    return grid, flashes


def print_grid():
    for row in grid:
        for val in row:
            if val == 0:
                print('x', end=' ')
            else:
                print(val, end =' ')
        print()
    print()

flashes_s = 0

i = 1
while True:
    grid, flashes_in_step = step(grid)
    if flashes_in_step == 100:
        print(i)
        break
    i += 1

