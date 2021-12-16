import math
from heapq import heappop, heappush, heapify

class Node:
    def __init__(self, pos, val, visited):
        self.pos = pos
        self.val = val
        self.visited = visited

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val

    def __str__(self):
        return f'({self.pos}:{self.val})'


def readfile(filename):
    with open(filename) as f:
        return list(map(lambda s: [int(x) for x in s.strip()], f.readlines()))


def expandcave(cave):
    tilew = len(cave[0])
    tileh = len(cave)

    expanded = [[0 for _ in range(tilew * 5)] for _ in  range(tileh * 5)] 

    for y, row in enumerate(cave):
        for x, val in enumerate(row):
            expanded[y][x] = val


    # filling row by row, from left to right
    for i in range(5): # 5 vertical tiles
        for j in range(5): # 5 horizontal tiles:
            for local_y in range(tileh):
                for local_x in range(tilew):
                    global_x = j*tilew + local_x
                    global_y = i*tileh + local_y

                    # ignore top left tile already filled
                    if expanded[global_y][global_x] != 0:
                        continue 

                    if j == 0: # 1st tile in row, need to fill from the top tile
                        prev_tile_x = global_x 
                        prev_tile_y = (i-1) * tileh + local_y
                    else: # filling from the left tile
                        prev_tile_x = (j-1) * tilew + local_x
                        prev_tile_y = global_y

                    prev_val = expanded[prev_tile_y][prev_tile_x]
                    val = prev_val + 1
                    if val == 10:
                        val = 1

                    expanded[global_y][global_x] = val 

    return expanded 


#cave = readfile('testinput')
cave = readfile('input1')
cave = expandcave(cave)

cavew = len(cave[0])
caveh = len(cave)

# for y, row in enumerate(cave):
#     if y % 10 == 0:
#         print()
#     for x, val in enumerate(row):
#         if x % 10 == 0:
#             print(' ', end='')
#         print(str(val), end='')
#     print()
# #    print(''.join(map(lambda x: str(x), row)))
# print()



#def relax(pos, cave, pathrisk):
#    # for now I assume you can only walk down and right 
#    x, y = pos
#    risk_at_pos = cave[y][x]
#
#    x_top, y_top = x, y-1
#    if y_top >= 0:
#        risk_from_top = pathrisk[y_top][x_top] + risk_at_pos
#        if risk_from_top < pathrisk[y][x]:
#            pathrisk[y][x] = risk_from_top
#
#    x_left, y_left = x-1, y
#    if x_left >= 0:
#        risk_from_left = pathrisk[y_left][x_left] + risk_at_pos
#        if risk_from_left < pathrisk[y][x]:
#            pathrisk[y][x] = risk_from_left
#
#

def walk(cave):
    pq = []
    nodes = []
    for i in range(0, caveh):
        nodes_row = [None for _ in range(cavew)]
        for j in range(0, cavew):
            if i == 0 and j == 0:
                continue

            n = Node((j, i), math.inf, False)
            nodes_row[j] = n
            heappush(pq, n)
        nodes.append(nodes_row)

    n = Node((0, 0), 0, False)
    nodes[0][0] = n
    heappush(pq, n)

    heapify(pq)

    i = 0 

    while len(pq) > 0:
        node = heappop(pq)
#        heapify(pq)

        print(i)
        i+=1
        
        
#        print('Popped: ', node)
#        for n in pq:
#            print(n)
#        print()

        x, y = node.pos

        x_top, y_top = x, y-1
        x_right, y_right = x+1, y
        x_down, y_down = x, y+1
        x_left, y_left = x-1, y

#        if y_top >= 0 and not nodes[y_top][x_top].visited:
#            dist = cave[y_top][x_top]
#            if dist + node.val < nodes[y_top][x_top].val:
#                nodes[y_top][x_top].val = dist + node.val

        if x_right < cavew and not nodes[y_right][x_right].visited:
            dist = cave[y_right][x_right]
            if dist + node.val < nodes[y_right][x_right].val:
                dohp = False
                if nodes[y_right][x_right].val == math.inf:
                    dohp = True

                nodes[y_right][x_right].val = dist + node.val

                if dohp:
                    heapify(pq)


        if y_down < caveh and not nodes[y_down][x_down].visited:
            dist = cave[y_down][x_down]
            if dist + node.val < nodes[y_down][x_down].val:
                dohp = False
                if nodes[y_down][x_down].val == math.inf:
                    dohp = True

                nodes[y_down][x_down].val = dist + node.val

                if dohp:
                    heapify(pq)

        if y_left >= 0 and not nodes[y_left][x_left].visited:
            dist = cave[y_left][x_left]
            if dist + node.val < nodes[y_left][x_left].val:
                dohp = False
                if nodes[y_left][x_left].val == math.inf:
                    dohp = True

                nodes[y_left][x_left].val = dist + node.val

                if dohp:
                    heapify(pq)

        node.visited = True

    return nodes



#    pathrisk[0][0] = 0
    

#    for i in range(1, cavew):
#        # check horizontal line)
#        for x in range(i+1):
#            relax((x, i), cave, pathrisk)
#        # check vertical line)
#        for y in range(i+1):
#            relax((i, y), cave, pathrisk)


#pathrisk[0][0] = 0

# print(cavew, caveh)

pathrisk = walk(cave)

#for row in pathrisk:
#    for node in row:
#        print(node.val, end =' ')
#    print()
#

print(pathrisk[caveh-1][cavew-1].val)
