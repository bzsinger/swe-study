# iterator

a = [2, 3, 4]
p = iter(a)
next(p)                 # 2
next(p)                 # 3
next(p)                 # 4
try:
    next(p)             # raises a StopIteration exception
except StopIteration:
    pass

# -------------------------------------------------------

a = [2, 3, 4]
p = iter(a)
type(p)                 # list iterator

# -------------------------------------------------------

a = [2, 3, 4]
p = iter(a)             # creates an iterator over the values in a
q = iter(a)
p is q                  # False - two different iterators

list(p) == [2, 3, 4]    # list's constructor takes an iterable
list(p) == []           # p is exhausted by the first constructor

list(q) == [2, 3, 4]    # p being exhausted is irrelevant to q

# -------------------------------------------------------

a = [2, 3, 4]
p = iter(a)
q = iter(p)             # same as doing q = p, copies a reference to p into q
list(p) == [2, 3, 4]
list(p) == []           # p is exhausted by the first constructor
list(q) == []           # q is exhausted because it is the same as p
p is q                  # True

# -------------------------------------------------------

r = range(2, 5)         # returns an iterator
                        # (in Python 3,) does not create a full list
                        # instead, returns values when needed
                        # construction is O(1), next is O(1)

list(r) == [2, 3, 4]
list(r) == [2, 3, 4]    # not exhaustible

# -------------------------------------------------------

for v in range(2, 5):   # internally has a try, except
    print(v)

# -------------------------------------------------------

a = [2, 3, 4]
# for v in a:
#     v += a              # integers (like strings, tuples, frozenset) are
#                         # immutable - this does not change the value of a


# -------------------------------------------------------

a = [2, 3, 4]
iter(a)                 # same as saying -
a.__iter__()

# -------------------------------------------------------

# iterables (ex. list, set, range) - **not exhaustible**

# iterators (ex. list iterator, range iterator, count, zip) - **exhaustible**
#   - lazy, constant time, constant space
#   - accomodates infinite structures (ex. count)

# see structures/add_properties.py
