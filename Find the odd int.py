def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num

if __name__ == '__main__':
    find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5])
    find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])
    find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5])
    find_it([10])
    find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1])
    find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10])

# story:
# create a loop for the list received
# create a counter to see how many times the number appears
# mod 2 to see if any remainder, if only one odd number as per question it will return a remainder of 1
# use .count to get number of duplicates element has in list

# source aid:
# https://stackoverflow.com/questions/20167108/how-to-check-how-many-times-an-element-exists-in-a-list

# alternate solution:

'''
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
'''