# Write a singleton class in Python.

class Singleton:
    def __init__(self, c):
        self.instance = c()
    def __call__ (self):
        return self.instance

@Singleton
class A1:
    pass

A1() == A1()
