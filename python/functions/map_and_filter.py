# map
# usage: map(<function>, <iterable>)

a = [2, 3, 4]
m = map(lambda x: x * x, a)     # lazy, constant effort
list(m) == [4, 9, 16]
list(m) == []                   # exhausted by the first list constructor

# -------------------------------------------------------

# filter
# usage: filter(<function>, <iterable>)

a = [2, 3, 4]
f = filter(lambda x: x % 2, a)  # only return elements that meet requirement
list(f) == [3]
list(f) == []                   # exhausted by the first list constructor

f = filter(lambda x: x % 2, a)  # only return elements that meet requirement
m = map(lambda x: x * x, f)     # returns mapped filter results
list(m) == [9]
list(f) == []                   # because map uses filter, map exhausts
list(m) == []                   #   both generators
