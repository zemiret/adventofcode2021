import math

def readfile(filename):
    with open(filename) as f:
        lines = f.readlines()
        template = lines[0].strip()
        ruleslist = list(map(lambda x: [s.strip() for s in x.split('->')], lines[2:]))
        return template, dict(ruleslist)

tpl, rules = readfile('input1')
# tpl, rules = readfile('testinput')

# print(tpl)
# print(rules)
#for rule in rules:
#    print(rule)
#print()

for i in range(10):
    new_tpl = ''
    pairs = list(zip(tpl, tpl[1:]))
    len_pairs = len(pairs)
    for j, pair in enumerate(pairs):
        if j == len_pairs - 1:
           new_tpl += pair[0] + rules[''.join(pair)] + pair[1]
        else:
           new_tpl += pair[0] + rules[''.join(pair)]

    tpl = new_tpl


counts = {}
for c in tpl:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1


minc = ('', math.inf)
maxc = ('', -math.inf)

for c, count in counts.items():
    if count < minc[1]:
        minc = (c, count)
    if count > maxc[1]:
        maxc = (c, count)


# print(minc, maxc)

print(maxc[1] - minc[1])
   
#print(len(tpl))
