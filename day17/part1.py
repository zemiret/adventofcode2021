# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
# import matplotlib.markers as markers
import math


def readfile(filename):
    with open(filename) as f:
        xmin, xmax, ymin, ymax = 0,0,0,0
        xs, ys = f.readline().strip().removeprefix('target area: ').split(',')
        xmin, xmax = [int(x) for x in xs.strip().removeprefix('x=').split('..')]
        ymin, ymax = [int(y) for y in ys.strip().removeprefix('y=').split('..')]
    
        return xmin, xmax, ymin, ymax


xmin, xmax, ymin, ymax = readfile('input1')

def did_overshoot(x, y):
    if x > xmax:
        return True
    if y < ymin:
        return True
    return False

def is_in_target(x, y):
    return xmin <= x <= xmax or ymin <= y <= ymax

def shot(v_x, v_y):
    x, y = 0, 0

    max_y = -math.inf
    while not did_overshoot(x, y):
        x += v_x
        y += v_y

        if y > max_y:
            max_y = y

        if is_in_target(x, y):
            return True, max_y

#        xs.append(x)
#        ys.append(y)

        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x  += 1
        v_y -= 1

    return False, -math.inf


max_y = -math.inf
for vx in range(1, 20):
    print(vx)
    for vy in range(100, 1000):
        reached, calculated_max = shot(vx, vy)
        if reached and calculated_max > max_y:
            max_y = calculated_max


print(max_y)


#rect = patches.Rectangle((xmin, ymin), (xmax-xmin), (ymax-ymin), linewidth=1, edgecolor='r', facecolor='none', fill=True)
#
#xs, ys = shot(10, 80, 200)
#_, ax = plt.subplots()
#ax.plot(xs, ys, marker='x')
#ax.add_patch(rect)
#plt.show()

# Aright, let's just try simulating V_x from 1 to 67 (more doesn't make sense cause it overshoots right away)
# y from 80 to 10000 

# def reaches_target(v_x, v_y):
    

