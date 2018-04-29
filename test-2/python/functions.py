# functions

def f(x, y, z):
    return [x, y, z]

f(2, 3, 4)              # [2, 3, 4] - can pass parameters by position
f(y=3, z=4, x=2)        # [2, 3, 4] - can pass parameters by position

# precedence
#   1. by position  -   non-dictionary unpacking
#   2. by named     -   dictionary unpacking

# ------------------------------------------------------------------------

# defaults
def f(x, y, z=3):       # if no argument passed in for z, uses value 3
    return [x, y, z]

f(1, 2, 4)  # [1, 2, 4]
f(1, 2)     # [1, 2, 3]

# must be last argument of function
# def f(x, y=3, z):     # SyntaxError

# mutable
def g(x=[]):
    x += [2]            # stores value between calls
    return x

g()         # [2]
g()         # [2, 2]
g(1)        # [1, 2] - different from default array because passed in
g()         # [2, 2]

# immutable
def h(x=()):
    x += (2)            # creates a new tuple because tuples are immutable
    return x

g()         # (2)
g()         # (2)
g(1)        # (1, 2)
g()         # (2)

# safe - None check
def k(x=None):
    if x is None:
        x = []
    x += [2]
    return x

# ------------------------------------------------------------------------

# keywords

def i(x, y, z):
    return [x, y, z]

i(2, y=3, z=4)         # must put non-keyword args before keyword args
                       # keyword args must match function args
                       # [2, 3, 4]

def j(x, *, y, z):     # only x is positional; y and z must be named
    return [x, y, z]

j(2, y=3, z=4)         # [2, 3, 4]
