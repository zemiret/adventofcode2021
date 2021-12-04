def most_common(lines, pos):
    zeros, ones = 0, 0
    for asd in lines:
        if asd[pos] == '1':
            ones += 1
        else:
            zeros += 1
    return ones > zeros and '1' or zeros > ones and '0' or ''

with open('input1') as f:
    lines = [x.strip() for x in f.readlines()]

    oxygen_lines = lines.copy()
    pos = 0
    while len(oxygen_lines) > 1:
        c = most_common(oxygen_lines, pos)
        if c == '':
            c = '1'
        oxygen_lines = list(filter(lambda x: x[pos] == c, oxygen_lines))
        pos += 1
        
    oxygen = int(oxygen_lines[0], 2)

    co2_lines = lines.copy()
    pos = 0
    while len(co2_lines) > 1:
        c = most_common(co2_lines, pos)
        if c == '':
            c = '1'
        co2_lines = list(filter(lambda x: x[pos] != c, co2_lines))
        pos += 1
        
    co2 = int(co2_lines[0], 2)
    print(oxygen * co2)
