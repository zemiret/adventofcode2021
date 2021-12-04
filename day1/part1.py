print(sum(map(lambda x: x[1] > x[0] and 1 or 0, zip([int(x) for x in open('input1').readlines()][:-1], [int(x) for x in open('input1').readlines()][1:]))))

