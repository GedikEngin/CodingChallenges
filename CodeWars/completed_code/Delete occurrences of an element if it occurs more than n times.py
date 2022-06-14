def delete_nth(order, max_e):
    for i in order:
        if order.count(i) > max_e:
            order.pop(i)

    return print(order)

if __name__ == '__main__':
    # delete_nth([20,37,20,21], 1)
    delete_nth([1,1,3,3,7,2,2,2,2], 3) # [1, 1, 3, 3, 7, 2, 2, 2])

# story:
# create a for loop
# counter for how many times it appears in it using 'in'
# if counter exceeds max_e remove

# sources
# https://stackoverflow.com/questions/20167108/how-to-check-how-many-times-an-element-exists-in-a-list
# https://stackoverflow.com/questions/53589457/typeerror-not-supported-between-instances-of-builtin-function-or-method-a