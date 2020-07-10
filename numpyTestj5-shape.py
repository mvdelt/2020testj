import numpy as np

a = np.arange(1,31).reshape(3,2,5)
print(a)
print(a.shape)
print(a.shape[:2])
# print(a.shape[:2]*0.5) # TypeError: can't multiply sequence by non-int of type 'float'
print((4,5,6,7)*5)
print(tuple(10*i for i in (4,5,6,7)))
print(tuple(10*i for i in (4,5,6,7)[:2]))
print(tuple(10*i for i in (4,5,6,7)[:2][::-1]))
print(tuple(10*i for i in (4,5,6,7)[:2:-1]))

