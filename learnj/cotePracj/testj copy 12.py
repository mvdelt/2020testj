def makefct(a,b):
    name = a
    age = 18
    def fctj(x):
        print(f'name:{name}, age:{age} x:{x}')
    return fctj

retfct = makefct('juny', 'this is not shown')

retfct('abc')