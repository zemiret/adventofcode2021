import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.markers as markers
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
    return xmin <= x <= xmax and ymin <= y <= ymax

def shot(v_x, v_y):
    initvx, initvy = v_x, v_y
    x, y = 0, 0

    xs, ys = [x], [y]

    max_y = -math.inf
    while not did_overshoot(x, y):
        x += v_x
        y += v_y

        xs.append(x)
        ys.append(y)

        if y > max_y:
            max_y = y

        if is_in_target(x, y):
#            print(x, y, 'vx, vy', initvx, initvy)
            return True, xs, ys 


        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x  += 1
        v_y -= 1

    return False, xs, ys
#    return False, -math.inf

rect = patches.Rectangle((xmin, ymin), (xmax-xmin), (ymax-ymin), linewidth=1, edgecolor='r', facecolor='none', fill=True)
#
#xs, ys = shot(10, 80, 200)
_, ax = plt.subplots()
ax.add_patch(rect)


all_reached = True

# minx that reaches anything is vx=7 with miny vy=-50 and maxy vy=259
# maxx that reaches anything is vx=67 with miny vy=-261 and maxy vy=-200

# y window to check
miny = -50
maxy = 259
count = 0

margin_width = 1000

for vx in range(7, 68): # all the xs that can reach the box
    print(vx)
    miny_reached = math.inf
    maxy_reached = -math.inf
    anything_reached = False


    for vy in range(miny - margin_width, maxy + margin_width):
        reached, xs, ys = shot(vx, vy)
        if reached:
            anything_reached = True
#            ax.plot(xs, ys, marker='x')
            if vy < miny_reached:
                miny_reached = vy
            if vy > maxy_reached:
                maxy_reached = vy

            count += 1

    if anything_reached:
        miny = miny_reached
        maxy = maxy_reached

print(count)
# plt.show()


# max_y = -math.inf
#for vx in range(67, 68):
# #   print(vx)
#    for vy in range(-200, -199):
#        reached, xs, ys = shot(vx, vy)
#        if reached:
#            anything_reached = True
#        if not reached:
#            all_reached = False
#        ax.plot(xs, ys, marker='x')
#        reached, calculated_max = shot(vx, vy)
#        if reached and calculated_max > max_y:
#            max_y = calculated_max

# print('Anything reached', anything_reached)
# print('All reached', all_reached)


# plt.show()

