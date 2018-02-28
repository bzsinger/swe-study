# set

## "Hash Set"
## order of elements does not matter
## each element is unique


x = set() # empty set -- { } is an empty dictionary
          # the only way to make an empty set is to use the constructor

x = {2, 3, 4}
len(x)                  # 3

x = {2, 3, 2}
len(x)                  # 2 - set does not allow duplicates

{1, 2, 3} == {3, 2, 1}  # order does not matter


s = {2, 3, 4}
t = set()
for v in s:
    t |= {v * 3}        # union-equals - unions two sets

t == {6, 9, 12}

# -------------------------------------------------------

# frozenset

# cannot add or remove values
f = frozenset() # empty frozenset

# no delimiter, need to use 'frozenset'
f = frozenset((2, 3, 4))
print(f)        # frozenset({2, 3, 4})

# data structure used to create frozenset doesn't matter
f = frozenset((2, 3, 4))
g = frozenset([2, 3, 4])
h = frozenset({2:"abc", 3:"def", 4:"ghi"})
f == g == h     # True

# to be in a set, an element must be hashable
# mutables - list, set, dictionary - **not** hashable
# immutables - str, int, bool, float, tuple, frozenset -- hashable
