def filter_list(list):
  filtered_list = []
  for element in list:
      if type(element) == int:
        filtered_list.append(element)
  return filtered_list



if __name__ == '__main__':
    filter_list([1,2,'a','b'])
    filter_list([1,'a','b',0,15])
# story:
# create a loop using list range
# have the element be compared to either see if it is in a numeric set or a alpha set
# add nums into list or remove letters from list
# return final list

#alternate solution:
''''''
def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]
'''

# sources used:
# https://www.pythonpool.com/check-data-type-python/