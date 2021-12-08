def readfile(filename):
    with open(filename) as f:
        return list(map(lambda y: [y[0].split(), y[1].split()], map(lambda x: x.split('|'), f.readlines())))


lines = readfile('input1')

def filter_seg(segments, note, include_segs, do_not_touch_segs=[]):
    for s in include_segs:
        segments[s] = ''.join((filter(lambda x: x in note, segments[s])))

    exclude_segs = [it for it in list(range(7)) if it not in include_segs and it not in do_not_touch_segs]
    for s in exclude_segs:
        segments[s] = ''.join((filter(lambda x: x not in note, segments[s])))

    return segments


number_to_segs = {
    0: [0,1,2,4,5,6],
    1: [2,5],
    2: [0,2,3,4,6],
    3: [0,2,3,5,6],
    4: [1,2,3,5],
    5: [0,1,3,5,6],
    6: [0,1,3,4,5,6],
    7: [0,2,5],
    8: [0,1,2,3,4,5,6],
    9: [0,1,2,3,5,6],
}

def segs_fired(segs_mapping, reading):
    fired = []
    for seg, letter in segs_mapping.items():
        if letter in reading:
            fired.append(seg)
    return sorted(fired)


def segs_to_number(segs):
    for num, num_segs in number_to_segs.items():
        if segs == num_segs:
            return num
    return None


def figure_segments(notes):
    segments = {i: 'abcdefg' for i in range(7)}

    notes = sorted(notes, key=len)

    for n in notes:
        if len(n) == 2: # 1
            segments = filter_seg(segments, n, [2,5])
        if len(n) == 4: # 4
            segments = filter_seg(segments, n, [1,2,3,5])
        if len(n) == 3: # 7
            segments = filter_seg(segments, n, [0,2,5])
        if len(n) == 6: # 0, 6, 9
            segments = filter_seg(segments, n, [0,1,5,6], [2,3,4])
        if len(n) == 5: # 2,3,5
            segments = filter_seg(segments, n, [0,3,6], [1,2,4,5])

    segments[2] = ''.join(filter(lambda x: x not in segments[5], segments[2]))
    segments[5] = ''.join(filter(lambda x: x not in segments[2], segments[5]))

    segments[4] = ''.join(filter(lambda x: x not in segments[6], segments[4]))
    segments[6] = ''.join(filter(lambda x: x not in segments[4], segments[6]))

    return segments


results = []
for i, line in enumerate(lines):
    notes = line[0]
    readings = line[1]
    mapping = figure_segments(notes)


    numstr = ''
    for reading in readings:
        fired = segs_fired(mapping, reading)
        num = segs_to_number(fired)
        numstr += str(num)

    results.append(int(numstr))

print(sum(results))
