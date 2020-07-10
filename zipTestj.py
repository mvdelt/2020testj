a = [3,6,9,12]
b = ['a','b','c']
# print(zip(a,b))
# print(zip(b,a))
print(dict(zip(a,b)))
print(dict(zip(b,a)))

for i in zip(b,a):
    print(i)

for i,j in zip(b,a):
    print(i,j)