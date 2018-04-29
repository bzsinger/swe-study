# equality
# == tests content, like Java's .equals method
5 == 5
[2, 3, 4] == [2, 3, 4] # see 'structures/list.py'
[2, 3, 4] == (2, 3, 4) # see 'structures/tuple.py'
{1, 2, 3} == {3, 2, 1} # see 'structures/set.py'

# 'is' tests identity, like Java's == operator
[2, 3, 4] is [2, 3, 4] # False

a = [2, 3, 4]
b = a
a is b                 # True

## for numbers between [-5, 256], 'is' behaves the same as ==
## for numbers < -5 or > 256, the integer is so large that it
## must be stored as an object
-5 is -5               # True
-6 is -6               # False

a = 256
b = 256
a is b                 # True

a = 257
b = 257
a is b                 # False

## for large positive literal numbers
## in variables, 'is' still works like ==
256 is 256             # True
257 is 257             # True

## for string literals, 'is' still works like ==
a = "abc"
a is "abc"             # True

a = "abc"
b = "abc"
a is b                 # True

s = "a"
t = "b"
u = "c"
a = s + t + u
b = "abc"
a is b                 # False

## == v. is for objects
class C:          # empty class
    pass

a = C()
b = C()
a is b            # False
a == b            # False -- C inherits parent's ==, which was
                  #           not overwritten, and is defined
                  #           as 'is'

class D:
    def __eq__(self, other):    # use to override ==
        pass
