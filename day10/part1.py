def readfile(filename):
    with open(filename) as f:
        return [x.strip() for x in f.readlines()]

scoring = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
}

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

illegal_chars = []

lines = readfile('input1')

def find_illegal(line):
    opening_stack = []

    for c in line:
        if c in opening:
            opening_stack.append(c)
        if c in closing:
            if not is_matching(opening_stack[-1], c):
                return c
            opening_stack.pop()
    


def score(illegal_chars):
    return sum(map(lambda x: scoring[x], illegal_chars))


for line in lines:
    c = find_illegal(line)
    if c is not None:
        illegal_chars.append(c)


print(score(illegal_chars))



# for line in lines:
#     print(line)
# print()

