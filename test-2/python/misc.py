# Miscellaneous Python functions

all(iterable)   # returns True if all of the elements in the iterable are True

any(iterable)   # returns True if any of the elements in the iterable are True

# can define functions inside other functions
def func1():
    def func2():
        return True
    return func2
