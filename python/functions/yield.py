# yield

# creates a generator
# all generators are iterators, not all iterators are generators
#   generators produce the values they will return - lazy
#   iterator iterates over already-created set of elements

def f():                # if function has 'yield' in it, it will not run
    print("abc")        #   instead, it will run every line up to the next
    yield 2             #   yield call and return the yielded value
    print("def")
    yield 3
    print("ghi")
    yield 4

a = f()                 # constant time operation
b = next(a)             # print "abc"
b == 2
b = next(a)             # print "def"
b == 3
b = next(a)             # print "ghi"
b == 4
try:
    b = next(a)         # raises StopIteration when it runs out
except StopIteration:
    ...

a = f()
list(a) == [2, 3, 4]    # also prints "abc" "def" "ghi"
list(a) == []           # exhausted by first list constructor
