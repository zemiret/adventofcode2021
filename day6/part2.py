def readfile(filename):
    with open(filename) as f:
        return list(map(lambda x: int(x), f.readline().split(',')))

def day_pass(buckets):
    new_fishes = buckets[0]

    # move all -1 pos
    for i in range(8):
        buckets[i] = buckets[i+1]
    buckets[8] = 0

    # add new_fishes to pos 6
    # add new_fishes to pos 8
    buckets[6] += new_fishes
    buckets[8] += new_fishes


fishes = readfile('input1')

buckets = {i:0 for i in range(9)}

for fish in fishes:
    buckets[fish] += 1


for i in range(256):
    day_pass(buckets)


print(sum(buckets.values()))
