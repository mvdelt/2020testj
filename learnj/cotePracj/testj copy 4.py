x = 10
def foo():
    global x
    print('1st:',x)
    x += 1
    print('2nd:',x)

foo()
print('x:',x)