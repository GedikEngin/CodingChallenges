def likes(names):

    if not names:
        return 'no one likes this'

    elif len(names) == 1:
        return names[0]+' likes this'

    elif len(names) == 2:
        return names[0]+' and '+names[1]+' like this'

    elif len(names) == 3:
        return names[0]+', '+names[1]+' and '+names[2]+' like this'

    elif len(names) >= 4:
        return names[0]+', '+names[1]+' and '+str(len(names) - 2)+' others like this'



if __name__ == '__main__':
    print(likes([]))
    print(likes(['John']))
    print(likes(['John', 'Benjamin']))
    print(likes(['John', 'Benjamin', 'Andrew']))
    print(likes(['John', 'Benjamin', 'Andrew', 'Socrates']))
    print(likes(['John', 'Benjamin', 'Andrew', 'Socrates', 'Clyde']))

# story
# create 5 if statements
# 1 -> 0 likes // no one likes this
# 2 -> 1 likes // x likes this
# 3 -> 2 likes // x and y like this
# 4 -> 3 likes// x, y and z like this
# 5 -> 4+ likes // x, y and * like this

# alternative solutions:
'''
def likes(names):
    l = len(names)
    if l == 0: return 'no one likes this'
    if l == 1: return '{} likes this'.format(names[0])
    if l == 2: return '{} and {} like this'.format(names[0], names[1])
    if l == 3: return '{}, {} and {} like this'.format(names[0], names[1], names[2])
    return '{}, {} and {} others like this'.format(names[0], names[1], len(names)-2)
'''