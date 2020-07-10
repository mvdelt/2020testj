class C:
    def __init__(self):
        # OK.
        super().__setattr__("foo", 1234444488888)

        # # AttributeError: 'super' object has no attribute 'foo'
        # setattr(super(), "foo", 123)
        # super().foo = 123123

class D(C):
    def __init__(self):
        # OK.
        super().__setattr__("foo_D", 999999876876)

        # AttributeError: 'super' object has no attribute 'foo'
        # setattr(super(), "foojjjjj", 1239999)
        # super().foo = 123123

c = C()
d = D()

print(c.__dict__)
print(C.__dict__)
# print(c.super())
setattr(c,"hahaj", 35555)
c.hahaj2 = 36666
setattr(C,"CaCa2",30302)
C.CaCa = 3030
print(c.__dict__)
print(C.__dict__)

print('d.__dict__:',d.__dict__)
print('D.__dict__:',D.__dict__)