import numpy as np

a = np.zeros(6)
# print(a)

b = np.zeros((2,3,5))
# print(b)

c = np.random.randint(10, size=(2, 3, 5))
d = np.random.rand(2, 3, 5)
print(c)
print(c[1][1][3])
print(c[1,1,3])
c[1,1,3] = 56.7
print(c) # i. 56.7 대신 56 이 있는걸 볼수있음.

print(d)
d[1,1,3] = 56.7
print(d)

print(b)
b[1,1,3] = 56.7
print(b)

for i in [a,b,c,d]:
    print('type({}) is {}, a.dtype is {}'.format(i, type(i), i.dtype))
# print(type(b))
# print(type(c))
# print(type(d))


