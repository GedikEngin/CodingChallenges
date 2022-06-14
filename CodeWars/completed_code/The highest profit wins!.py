def min_max(lst):
    profit = []
    min_val = lst[0]
    max_val = 0
    for val in lst:
        if val < min_val:
            min_val = val
        elif val > max_val:
            max_val = val
    profit.append(min_val)
    profit.append(max_val)
    return profit

if __name__ == '__main__':
    min_max([1, 2, 3, 4, 5])
    min_max([2334454, 5])

# story
# have a min and max variable
# compare for values in lst
# if smaller than min, assign to min
# if larger than max assign to max
# else ignore

# alternate solution:
'''
def min_max(lst):
  return [min(lst), max(lst)]
'''