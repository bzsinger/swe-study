# decorators

# function decorator

# without decorators
def f1(n):
    return n+1

def fd(g):
    # creates wrapper around g that shows its input and output
    def h(n):
        print("input ", n)
        m = g(n)  # disclaimer: need to know nature of f1 to mimic its API
        print("output ", n)
        return m
    return h

f2 = fd(f1) # f2 is h with f1 passed in

f1 = fd(f1) # f1 is now h with the original f1 function passed in

# with decorators
@fd             # calls fd with f3 as the parameter and stores the
def f3(n):      #   result back into f3
    return n+1

# can put a decorator in front of any function with the same API
#   can use to separate two logical components (ex. Collatz, caching)
# decorator must be callable

# ------------------------------------------------------------------------

# class decorator

# without decorators
class A1:
    pass

x = A1()
y = A1()
x == y      # False - A1 does not override ==
type(A1)    # type
type(x)     # A1

def sd(c): # parameter is a class
    x = c()
    return lambda : x  # return function that returns the single specific
                        #   instance of A1

A2 = sd(A1)
type(A2)  # function

x2 = A2()
type(x2)  # A1
y2 = A2()
type(y2)  # A1
x2 == y2  # True - same object (captured by closure)

# with decorators
@sd       # sd turns class insto a Singleton
class A3:
    pass

type(A3) # function
