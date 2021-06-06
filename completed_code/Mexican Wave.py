def wave(string):
    new = []
    for i, val in enumerate(string[:]): # i is the character position, e is the character itself
        if val != ' ':
            up = string[i].upper() # turns case i into capital
            c = string[:i] + up + string[i + 1:] # replaces the string with
            new.append(c) # append the new string with c
    return new

if __name__ == '__main__':
    wave('testing')
    wave('exceptional')
    wave('boo')


# story:
# grab the length of the string
# set string[i] (first letter, second letter etc) to be capital
# append into a list

# aid:
# https://stackoverflow.com/questions/46353162/mexican-wave-effect-in-python