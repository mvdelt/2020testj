def argTest(a,b,c='hi',d='jun',e='great!!!'):
    print('a:',a)
    print('b:',b)
    print('c:',c)
    print('d:',d)
    print('e:',e)

def call_argTest(*args_j, **kwargs_j):
    print(f'args_j: {args_j}')
    print(f'type args_j: {type(args_j)}')
    print(f'kwargs_j: {kwargs_j}')
    print(f'type kwargs_j: {type(kwargs_j)}')
    return argTest(*args_j, c='i am c!!', **kwargs_j)

call_argTest('im a', 'im b', d='im dddd', e='im eeeeee')