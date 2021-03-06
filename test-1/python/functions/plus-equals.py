# += operator

int j = 2
int k = j + 1       # addition operator
                    # requires two 'r-values'

j += k              # j == 5
                    # modifies j
j += 2              # j == 7

# 2 += 2            # **does not** work
                    # += needs an 'l-value'

# int k = (i += j)  # works in Java, C, C++
                    # *does not** work in Python

# in Python, if an operator changes one of its arguments,
#   it returns nothing
# thus, there is **no** ++ operator in Python

# -------------------------------------------------------

"""
valid on the left-hand-side of assignment, you're an l-value
if not, you're an r-value
i is an l-value
2 is an r-value
"""
i = 2

"""
+ takes two r-values
+ is an expression, cannot stand alone

i += j
i += 2
3 += 2  # does not work
"""


"""
+= takes an l-value on the left and an r-value on the right
+= can stand alone, is a statement

in Python, returns nothing
in C and Java, returns an r-value
in C++, returns an l-value
"""

"""
k = ++i     # puts value of **incremented** i into k,
k = i++     # puts **old** value of i into k
            #    needs to make a copy of i and return old value
            #    - **more expensive**

for (int i = 0; i != s; i++)   # compiler in Java, C, C++ rewrites i++ to ++i
                               #    because making the copy is expensive

for (T i = 0; i !=s; i++)      # compiler **cannot** rewrite because ++ is user
                               #    defined

(i += j) = k                   # works in C++, **does not** work in
                               #    Java, C, Python

++++i                          # works in C++, **does not** work in
                               #    Java, C, Python

i++++                          # doesn't work in any language
"""

# -------------------------------------------------------

# list's +=
## takes an iterable on the right, **asymmetric**
a = [2, 3, 4]
a += [5]
a == [2, 3, 4, 5]       # True

a += (6, )
a == [2, 3, 4, 5, 6]    # True - list's += **does not** require a list

# tuple's +=
## take a tuple on the right, **symmetric**
a = (2, 3, 4)
a += (5, )
a == (2, 3, 4, 5)       # True

# a += [6]              # **does not* work, tuple's += is stricter because
                        # it creates a **new** tuple

# list's ___ + ____
## takes a list on the right, **symmetric**
a = [2, 3, 4]
# a = a + (5, )        # **does not* work, list's __ + __ is stricter because
                       # it creates a **new** list

# -------------------------------------------------------

## += and ___ + ___ have the **same meaning** for **immutables**
##                      - create a new data structure
##                  have a **different** meaning for **immutables**
##                      += - store in current, __ + __ - create new
