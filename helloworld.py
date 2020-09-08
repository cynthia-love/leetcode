

class A:
    def __init__(self):
        pass

    def f(self):

        return B()

class B:
    def __init__(self):
        self.a = A()


a = A()
print(a.f())