def max_sequence(arr):
    neg_arr = False
    empty_arr = False
    total_val = 0
    for num in arr:
        if num > 0:
            total_val += num
    print(total_val)

if __name__ == '__main__':
    max_sequence([3,6,1,3,6])
    max_sequence([])
    max_sequence([0])
    max_sequence([-1, -2, -7, -4])
    max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])


# story:
# check if the array is composed of
# A) nothing
# B) only negatives
# C) mixed
# D) just positive