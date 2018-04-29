# replication

s = [1, 2, 3]
2 * s == [1, 2, 3, 1, 2, 3]

s = "abc"
2 * s == "abcabc"

s = (1, 2, 3)
2 * s == (1, 2, 3, 1, 2, 3)

## **does not** work for set, frozenset, dict

# copy
from copy import copy

u = (1, 2, 3)
v = copy(u)
u is v          # True - tuples are immutable, no reason to copy
                #   just returns reference to original tuple

u = [1, 2, 3]
v = copy(u)
u is v          # False
u == v          # True

u = [1, [1, 2, 3], 3]
v = copy(u)
u is v          # False
u == v          # True
u[1] is v[1]    # True - only copies reference

# deepcopy
from copy import deepcopy

u = [1, [1, 2, 3], 3]
v = deepcopy(u)
u is v          # False
u == v          # True
u[1] is v[1]    # False - follows all references and makes copies

# indexing
a = [1, [1, 2, 3], 3]
b = a[:]
b is a          # False - makes copy
a[1] is b[1]    # True - only copies reference
