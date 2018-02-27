# types

## list
a = [2, 3, 4]
type(a)         # list
x = [2]                # single item list
type(x)         # list

# -------------------------------------------------------

## tuple
a = (2, 3, 4)
type(a)         # tuple
x = (2, )             # single item tuple -- notice the ,
type(x)         # tuple

x = (2)         # int - (...) used for grouping, not the same
                #               property as [...]
type(x)         # int

# -------------------------------------------------------

type(list)      # type
type(type)      # type

# -------------------------------------------------------

a = [2, 3, 4]
type(a)         # list
p = iter(a)
type(p)         # list iterator


a = {2, 3, 4}
type(a)         # set
p = iter(a)
type(p)         # set iterator

a = {2: "abc", 3: "def", 4: "ghi"}
type(a)         # dict
p = iter(a)
type(p)         # dict key iterator
