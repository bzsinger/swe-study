# list

a = [2, 3, 4]
b = [2]         # single item list

## adding to the end of a list takes amortized constant time
## lists are "front-loaded" - there's extra space in the back for
##      new elements
a += [5]

## indexing
a[1] == 3
a[-1] == 4          # asymmetric - 0 is first from left, -1 is first from right

a[1:2] == [3]       # get elements from index [1, 2)
a[1:3] == [3, 4]    # get elements from index [1, 3)
a[0:3:2] == [2, 4]  # get every 2nd element from [0, 3)
a[:] == [2, 3, 4]   # get all elements
