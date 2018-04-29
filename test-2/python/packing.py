# packing

# *
def f(x, y, *z):        # can only have 1 starred argument in function
    return [x, y, z]    #   definition
                        # places remaining arguments into tuple
                        # must be final parameter (or penultimate if followed by
                        #    ** )

                        # cannot pass arguments into z - name *only known* to f

# **
def g(x, y, **z):       # must be final parameter
    return [x, y, z]    # places remaining arguments into dictionary
                        # only packs parameters passed by name

g(2, 3)              # [2, 3]
g(2, 3, a=2, b=3 )   # [2, 3, {"a": 2, "b": 3}]

d = {"x": 2, "y": 3}
g(**d)               # [2, 3, {}] - arguments get used up by named parameters

# ------------------------------------------------------------------------

def h(x, y, z=4, *t, **d):      # x, y, z - visible from outside
                                #   - can pass in argument by name
    return [x, y, z, t, d]      # t - non visible from outside
                                #   - cannot pass in argument by name
                                # d - all arguments passed as "d" get added to
                                #   d's dictionary packing

u = (5, 6)
h(2, t=9, *u)   # [2, 5, 6, (), {"t": 9}]
