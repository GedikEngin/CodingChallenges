def longest(a1, a2):
    string = ''
    for char in a1:
        if char not in string:
            string += char
    for char in a2:
        if char not in string:
            string += char
    return ''.join(sorted(string))

if __name__ == '__main__':
    longest("aretheyhere", "yestheyarehere")
    longest("loopingisfunbutdangerous", "lessdangerousthancoding")

# story:
# for i in a1/a2
# check if it is in the final string
# add to the string if not in it

# sources:
# https://www.geeksforgeeks.org/python-ways-to-sort-letters-of-string-alphabetically/