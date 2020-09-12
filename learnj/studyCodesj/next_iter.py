strj = "a b12 c dd eee"
li = strj.split()
print(f'li: {li}') # li: ['a', 'b12', 'c', 'dd', 'eee']

iter_li = iter(li)
print(f'type(iter_li): {type(iter_li)}') # type(iter_li): <class 'list_iterator'>
print(f'iter_li: {iter_li}') # iter(li): <list_iterator object at 0x0000022E8649F048>

nextVal = next(iter_li)
print(f'type(nextVal): {type(nextVal)}') # type(nextVal): <class 'str'>
print(f'nextVal: {nextVal}') # nextVal: a

nextVal = next(iter_li)
print(f'type(nextVal): {type(nextVal)}') # type(nextVal): <class 'str'>
print(f'nextVal: {nextVal}') # nextVal: b12




# aa = ['a','b','4','5','6','c','7']
# print(' '.join(aa))   # a b 4 5 6 c 7


            
