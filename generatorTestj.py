def somf():
    yield 'hoho'
    yield 'hoho2'
    yield 'hoho3'

print(somf) # i. somf is just a *function*. 
print(somf()) # i. the return(?) value of somf is a *generator*. (I put question mark at 'return' cuz there is no 'return' in somf.)

print(next(somf()))
print(next(somf()))
print('somf()',somf())
print(next(somf()))
print(next(somf()))

print('-----------------------')

a = somf()
print('a:',a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))