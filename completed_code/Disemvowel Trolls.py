
def disemvowel(string):
    return ''.join([letter for letter in string if letter not in 'aeiouAEIOU'])


if __name__ == '__main__':
    (disemvowel('Hello this is an exceptional programming'))