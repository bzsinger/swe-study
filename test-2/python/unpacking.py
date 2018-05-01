# unpacking

def f(x, y, z):
    return [x, y, z]

f(2, 3, 4)              # [2, 3, 4] - can pass parameters by position
f(y=3, z=4, x=2)        # [2, 3, 4] - can pass parameters by position

# precedence
#   1. by position  -   non-dictionary unpacking
#   2. by name      -   dictionary unpacking

# ------------------------------------------------------------------------

def f(x, y, z):
    return [x, y, z]

# * - requires iterables

t = (3, 4)
f(2, *t)    # [2, 3, 4]
f(*t, 2)    # [3, 4, 2] - can do unpacking before position

# f(x=2, *t)    # * has higher precedence than pass by name, gets multiple
                #   values for x

f(z=7, *t)  # [3, 4, 7] - can pass by name before unpacking

# ------------------------------------------------------------------------

# ** requires dict (or something like it)
#   keys must have same names as function parameters

d = {'z': 4, 'y': 3, 'x': 2}
f(**d)     # [2, 3, 4]

# f(x=2, **d)   # gets conflicting values for x

e = {'z': 4, 'y': 3}
f(2, **e)  # because no x in dict, can consume first argument by position

# f(**d, 2)         # cannot unpack dictionary before position
# f(**d, *t, y=2)   # cannot unpack dictionary before iterable unpacking

# ------------------------------------------------------------------------

# can also unpack into dictionary constructors
d = {'z': 4, 'y': 3, 'x': 2}
e = {'w': 0, 'v': 1}

z = {**e, **d}      # {'w': 0, 'v': 1, 'z': 4, 'y': 3, 'x': 2}
