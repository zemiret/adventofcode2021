from functools import reduce
import operator

def get_cols(board):
    cols = []
    for i in range(len(board[0])):
        col = [row[i] for row in board]
        cols.append(col)
    return cols

def check_entity_win(arr):
    return reduce(operator.mul, map(lambda p: p[1], arr))

def mark(board, number):
    for row in board:
        for p in row:
            if p[0] == number:
                p[1] = True

def check_board_win(board):
    for row in board:
        if check_entity_win(row):
            return True

    for col in get_cols(board):
        if check_entity_win(col):
            return True


def readfile(filename):
    with open(filename) as f:
        lines = f.readlines()
        calls = [int(x) for x in lines[0].strip().split(',')]

        boards = []
        cur_board = []
        for line in lines[2:]:
            if line.strip() == '':
                boards.append(cur_board)
                cur_board = []
            else:
                cur_board.append([[int(x), False] for x in line.split()])

        return calls, boards


def print_board(board):
    for row in board:
        print(list(map(lambda x: x[0], row)))

    for row in board:
        print(list(map(lambda x: x[1], row)))


calls, boards = readfile('input1')

def get_winner():
    for call in calls:
        for board in boards:
            mark(board, call)

            if check_board_win(board):
                return call, board

wincall, winner = get_winner()

s = 0
for row in winner:
    for val in row:
        if val[1] == False:
            s += val[0]

print_board(winner)

print(s)
print(wincall)
print(s * wincall)


