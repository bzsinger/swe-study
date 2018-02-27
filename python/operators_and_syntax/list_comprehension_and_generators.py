# list comprehension

a = [2, 3, 4]
b = [x * x for x in a]                # list comprehension
b == [4, 9, 16]

s = {2, 3, 4}
t = {x * 5 for x in a}                # set comprehension
t == {10, 15, 20}

d = {2: "a", 3: "b", 4: "c"}
e = {k + 1: d[k] + "xyz" for k in d}  # dict comprehension (over keys in d)
e == {3: "axyz", 4: "bxyz", 5: "cxyz"}



g = (x * x for x in a)  # generator
list(g) == [4, 9, 16]
list(g) == []           # exhausted by first list constructor

g = (x * x for x in a if x % 2)
list(g) == [9]
list(g) == []
