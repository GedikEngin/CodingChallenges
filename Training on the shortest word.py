def find_short(string):
    word_lst = []
    short = 9999
    word_lst = string.split(' ')
    for word in word_lst:
        if short > len(word):
            short = len(word)
    return short

if __name__ == '__main__':
    find_short('Hello this is a testing string to grab the letter a')
    find_short('Exceptional programming talent is very difficult to encounter in saturated environment')
    find_short('Deltoid unfathomable distinguished fabulous')

# story:
# create a list using the split function
# for word in lenword
# ^^ use to grab string length
# assign to a variable that has the shortest word length (len_word)
# return

# sources used:
#https://www.w3schools.com/python/ref_string_split.asp#:~:text=Python%20String%20split%20%28%29%20Method%201%20Definition%20and,how%20many%20splits%20to%20do.%204%20More%20Examples

# alternate solution:
'''
def find_short(s):
    return min(len(x) for x in s.split())
'''
# works by splitting the string in a nested for loop and uses the x for min comparison