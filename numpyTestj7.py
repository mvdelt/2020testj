import numpy as np

k=17

z = np.zeros((k))

print(z)

a = np.array([2,3,4,5,0,-3,-6])
print(1-a)
b = np.zeros((7))
m = np.max((b,1-a),axis=0)
print(m)

vg = np.array([2,0,1,0,1,2,2])
print(vg>0)
k1 = np.count_nonzero(vg>0)
print(k1)

e = np.array([1,2,3,4,5,6,7])
print(e[vg>0])

print(np.spacing(5))
print(np.spacing(1))
print(np.spacing(0))

arr1 = np.random.randint(1,10,(3,4))
print(arr1)

# for i in range(arr1.shape[0]):
#     for j in range(arr1.shape[1]):
#         print(arr1[i,j])   # i. 잘 작동.

ious = {(k, l): arr1[k, l] \
                for k in range(3)
                for l in range(4)}
print('ious:',ious)

for i in range(arr1.shape[0]):
    for j in range(arr1.shape[1]):
        print('ious[{},{}]: {}'.format(i,j,ious[i,j]))  # i. 잘 작동.



