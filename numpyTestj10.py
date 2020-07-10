import numpy as np

arr1 = np.random.randint(10, size=(2, 3, 5))
arr2 = np.random.randint(10, size=(2, 3, 5))

print(arr1)
print(arr2)

for i in zip(arr1, arr2):
    print(i)