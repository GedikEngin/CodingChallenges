def is_valid_walk(walk):
    x_cord = 0
    y_cord = 0
    if len(walk) != 10:
        return False
    for motion in walk:
        if motion == 'n':
            x_cord += 1
        if motion == 's':
            x_cord -= 1
        if motion == 'e':
            y_cord += 1
        if motion == 'w':
            y_cord -= 1

    if x_cord == 0 and y_cord == 0:
        return True
    else:
        return False

# story:
# go through each element in the instruction list
# have 2 variables used to simulate x and y coordinates
# 0, 0 is origin
# check if list len is exactly 10 at beginning to make sure it is optimized

if __name__ == '__main__':
    print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s'])) # true
    print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s'])) # false

# alternate solution:
'''
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
'''