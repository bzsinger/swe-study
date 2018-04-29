# unpacking

def f(x, y, z):
    return [x, y, z]

# * - requires iterables

t = (3, 4)
f(2, *t)    # [2, 3, 4]
f(*t, 2)    # [3, 4, 2]

# f(x=2, *t)    # * has higher precedence than pass by name, gets multiple
                #   values for x

# ------------------------------------------------------------------------

# ** requires dict (or something like it)
#   keys must have same names as function parameters

d = {"z": 4, "y": 3, "x": 2}
f(**d)     # [2, 3, 4]
