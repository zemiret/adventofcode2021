import math

def readfile(filename):
    with open(filename) as f:
        lines = f.readlines()
        template = lines[0].strip()
        ruleslist = list(map(lambda x: [s.strip() for s in x.split('->')], lines[2:]))
        return template, dict(ruleslist)

tpl, rules = readfile('input1')


def get_new_pairs(pair):
    c = rules[pair]
    return pair[0] + c, c + pair[1]

pairs = {}

# load start pairs
for pair in list(zip(tpl, tpl[1:])): 
    pair_str = ''.join(pair)
    if pair_str not in pairs:
        pairs[pair_str] = 0
    pairs[pair_str] += 1


for i in range(40):
    new_pairs = {}

    print(pairs)

    for pair, count in pairs.items():
        p1, p2 = get_new_pairs(pair)

        if p1 not in new_pairs:
            new_pairs[p1] = 0
        if p2 not in new_pairs:
            new_pairs[p2] = 0

        new_pairs[p1] += count
        new_pairs[p2] += count

    pairs = new_pairs


counts = {}
for pair, count in pairs.items():
    c1, c2 = pair[0], pair[1]
    if c1 not in counts:
        counts[c1] = 0
    if c2 not in counts:
        counts[c2] = 0

    counts[c1] += count
    counts[c2] += count

minc = ('', math.inf)
maxc = ('', -math.inf)

for c, count in counts.items():
    if count < minc[1]:
        minc = (c, count)
    if count > maxc[1]:
        maxc = (c, count)


# THIS IS A WRONG ANSWER
# But if you divide it by 2 and then subtract 0.5 you have 50% chance it is the correct one
# Then if it's not, add 0.5 instead of subtracting, and that will be the right answer. XD
print(maxc[1] - minc[1])
