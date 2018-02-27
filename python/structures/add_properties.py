# adding properties to a class

# constructor

class A:
    def __init__(self):     # called when creating a new A()
        ...                 # otherwise would use object's constructor

# -------------------------------------------------------

# indexable
class A:
    def __getitem__(self, index):      # make class 'indexable'
        ...                            # implement __getitem__

f = A()
f[3]                # can index into f because it's an 'A', same as -
f.__getitem__(3)

# -------------------------------------------------------

# iterable
def MyIterator:
    def __iter__(self):                # return an iterator over the class
        ...                            #    instance

# iterator
    def __next__(self):                # define next(...) method
        ...                            # by convention, should raise
                                       #    StopIteration when nothing left
                                       #    to return
