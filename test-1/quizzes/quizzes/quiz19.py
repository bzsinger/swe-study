# what is the output of the following?
def test1 () :
    a  = [2, 3, 4]
    b  = [v + 1 for v in a]
    a += [5]
    print(list(b), end=" ")
    print(list(b))

# what is the output of the following?
def test2 () :
    a = [2, 3, 4]
    b = (v + 1 for v in a)
    a = [2, 3, 4, 5]
    print(list(b), end=" ")
    print(list(b))
