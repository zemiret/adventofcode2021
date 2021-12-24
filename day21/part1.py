pos1 = 10
pos2 = 9

rolls = 0


def get_dice():
    global rolls
    dice = 1
    while True:
        rolls += 1
        yield dice
        dice += 1
        if dice == 101:
            dice = 1




dice = get_dice()

score1 = 0
score2 = 0

def round():
    global pos1, pos2, score1, score2, dice

    rolls1 = next(dice) + next(dice) + next(dice)
    pos1 = (pos1 + rolls1) % 10
    if pos1 == 0:
        pos1 = 10
    score1 += pos1
    if score1 >= 1000:
        return
    

    rolls2 = next(dice) + next(dice) + next(dice)
    pos2 = (pos2 + rolls2) % 10
    if pos2 == 0:
        pos2 = 10
    score2 += pos2
    if score2 >= 1000:
        return


while score1 < 1000 and score2 < 1000:
    round()


if score1 >= 1000:
    print(score2 * rolls)
else:
    print(score1 * rolls)

