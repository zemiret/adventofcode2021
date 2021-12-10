def readfile(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]

opening = '([{<'
closing = ')]}>'

def is_matching(op, c):
    if op == '(':
        return c == ')'
    elif op == '[':
        return c == ']'
    elif op == '<':
        return c == '>'
    elif op == '{':
        return c == '}'

def get_matching(op):
    if op == '(':
        return ')'
    elif op == '[':
        return ']'
    elif op == '<':
        return '>'
    elif op == '{':
        return '}'

def find_illegal(line):
    opening_stack = []

    for c in line:
        if c in opening:
            opening_stack.append(c)
        if c in closing:
            if not is_matching(opening_stack[-1], c):
                return c
            opening_stack.pop()
    
def get_closings(line):
    opening_stack = []

    for c in line:
        if c in opening:
            opening_stack.append(c)
        if c in closing:
            if not is_matching(opening_stack[-1], c):
                print('SOMETHING IS MESSED UP!!!')
            opening_stack.pop()

    return list(map(lambda x: get_matching(x), reversed(opening_stack)))


def score_line(closings):
    scoring = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    s = 0
    for c in closings:
        s = s * 5 + scoring[c]
    return s




lines = readfile('input1')
incomplete_lines = [line for line in lines if find_illegal(line) is None]
scores = sorted([score_line(get_closings(line)) for line in incomplete_lines])


print(scores[int((len(scores)-1)/2)])

