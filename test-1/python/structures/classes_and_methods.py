# class
class A:
    # function definition
    def f (self): # every method (function that will be called with an object)
                  # requires self as first parameter
                  # self is a reference to the object you invoke the method on
        ...       # using 'self' is convention - can use any word

def g ():         # outside of a class, functions do not need
                  #     a 'self' parameter

# dynamically typed
x = A()
y = A()
z = A()

isinstance(z, A)      # True

x.f() # self is x
y.f() # self is y

# inheritance
class B(A):           # class B inherits from class A
    ...

issubclass(B, A)      # True

# every class automatically inherits from object
issubclass(A, object) # True

# globals
h = 0

def f (...) :
    global h         # access the 'h' variable
    ...
