with open('input1') as f:
    lines = [x.strip() for x in f.readlines()]

    gamma_bin = ''
    eps_bin = ''
    for pos in range(len(lines[0])):
        zeros = 0
        ones = 0
        for p in lines:
            if p[pos] == '0':
                zeros += 1
            else:
                ones += 1

        if ones > zeros:
            gamma_bin += '1'
            eps_bin += '0'
        else:
            gamma_bin += '0'
            eps_bin += '1'

    gamma = int(gamma_bin, 2)
    eps = int(eps_bin, 2)

    print(gamma * eps)

