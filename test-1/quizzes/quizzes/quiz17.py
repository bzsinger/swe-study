# what is the output of the following?
def f () :
    yield 2
    yield 3
    yield 4

print(list(f()), end=" ")
print(list(f()), end=" ")
p = f()
q = iter(p)
print(p is q)

# what is the output of the following?
def g (b, e) :
    while b != e :
        yield b
        b += 1

print(list(g(2, 5)), end=" ")
print(list(g(2, 5)), end=" ")
p = g(2, 5)
q = iter(p)
print(p is q)
