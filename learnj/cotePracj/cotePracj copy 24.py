
class A():
    pass

a = A()

if a.something == None:
    print('it is None') # i. AttributeError: 'A' object has no attribute 'something'