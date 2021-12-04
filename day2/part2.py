with open('input1') as f:
    inst = list(map(lambda x: (x[0], int(x[1])), [y.split() for y in f.readlines()]))
    dep, hor, aim = 0, 0, 0
    for asd in inst:
        aim += (asd[0] == 'down' and asd[1] or asd[0] == 'up' and -asd[1] or 0)
        hor += (asd[0] == 'forward' and asd[1] or 0)
        dep += (asd[0] == 'forward' and aim * asd[1] or 0)
    print(hor * dep)
