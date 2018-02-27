# range

r = range(10)   # iterator that produces values from [0, 10)
r[0] == 0       # range is 'indexable'
r[9] == 9
# r[10] == 10   # **does not** work

# r[0] = 3      # **does not** work, range is immutable

list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(r) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # inexhaustable

# -------------------------------------------------------

# count

# usage: count(<seed>, <step>), default - count(0, 1)

from itertools import count
c = count()     # returns iterator, lazily counts forever - 0, 1, 2, 3...
# c[3] == 3     # **does not** work - **not** indexable

c = count(3, 2) # count forever, **starting at** 3 **by** 2s - 3, 5, 7
next(c)         # 3
next(c)         # 5

# -------------------------------------------------------

# zip
# usage: zip(<iterable>, <iterable>, ...)

# takes n iterables and returns an iterator the provides a tuples
z = zip([2, 3], [4, 5, 6])
list(z) == [(2, 4), (3, 5)]     # stops when shorter iterable stops
list(z) == []                   # exhausted by first list constructor

from itertools import count
z = zip([2, 3], count())
list(z) == [(2, 0), (3, 1)]     # stops when shorter iterable stops
list(z) == []                   # exhausted by first list constructor
