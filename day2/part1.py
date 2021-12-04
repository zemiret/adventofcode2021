print(sum(map(lambda x: x[0] == 'down' and x[1] or x[0] == 'up' and -x[1] or 0 , list(map(lambda y: (y[0], int(y[1])), [x.split() for x in open('input1').readlines()])))) * sum(map(lambda x: x[0] == 'forward' and x[1] or 0 , list(map(lambda y: (y[0], int(y[1])), [x.split() for x in open('input1').readlines()])))))


