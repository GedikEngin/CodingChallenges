
def spin_words(sentence):
    sentence = sentence.split()
    for words in range(len(sentence)):
        if len(sentence[words]) > 4:
            split_words = sentence[words].split(' ')
            reversed_word_list = [word[::-1] for word in split_words]
            sentence[words] = reversed_word_list[0]
    sentence = (' '.join(sentence))

    return sentence



# story:
# put words into a list
# get index word and see word length
# if word length is >4, enter for loop
# where it gets each character from tail end
# assign the inverse character order into a string
# replace the item in the list

if __name__ == '__main__':
    print(spin_words('This is an exceptional programming solution'))


# source aids:
# https://stackoverflow.com/questions/931092/reverse-a-string-in-python
# https://www.programiz.com/python-programming/methods/built-in/reversed
# https://www.geeksforgeeks.org/python-reverse-word-sentence/
# https://www.statology.org/replace-values-in-list-python/
# https://www.askpython.com/python/string/remove-character-from-string-python

# solution 1:
'''
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)
'''

# solution 2:
'''
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
'''