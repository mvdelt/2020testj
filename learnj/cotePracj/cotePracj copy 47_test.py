# print(len({1:2, 2:23, 3:333}))

a = [set([1,3,5,7])-set([1,5,7,8,9])][0]
print(a)

b = next(iter(set([1,3,5,7])-set([1,5,7,8,9])))
print(b)

for v in [2,4,6,8]:
    v *= 10
    print(v)