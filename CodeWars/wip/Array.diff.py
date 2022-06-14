
def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)
    return a

if __name__ == '__main__':
    array_diff([1, 2, 3], [1, 2])
