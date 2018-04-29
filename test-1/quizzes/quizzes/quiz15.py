# what is the output of the following?
def test1 () :
    a = [2, 3, 4]
    print(list(a), end=" ")
    print(list(a))

# what is the output of the following?
def test2 () :
    a = [2, 3, 4]
    p = iter(a)
    print(list(p), end=" ")
    print(list(p))

# what is the output of the following?
def test3 () :
    a = [2, 3, 4]
    p = iter(a)
    print(p is a, end=" ")
    q = iter(p)
    print(q is p)
