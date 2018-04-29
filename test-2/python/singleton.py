class Singleton:
    def __init__(self, c):
        self.instance = c()

    def __call__(self):
        return self.instance


@Singleton
class Foo:
    pass


a = Foo()
b = Foo()
print(a == b)
