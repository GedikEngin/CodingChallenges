def reverse_words(string):
    string = string.split(' ')
    new_str = []
    for char in range(len(string)):
        new_str.append((string[char][::-1]))
    return ' '.join(new_str)




    # words = list(reversed(words))
    # print(" ".join(words))

if __name__ == '__main__':
    print(reverse_words('I want to kill myself'))

# aid material:
# https://www.tutorialspoint.com/reverse-words-in-a-given-string-in-python

# alternative solution:
'''
def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' ')) # you can keep the split params clear as an alternative way
'''