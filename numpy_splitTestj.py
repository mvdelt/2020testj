import numpy as np

arr1 = np.random.randint(100, size=(10, 3, 5))

print(arr1)

arr1_split = np.split(arr1, [4], axis=2) # i. 파이토치의 텐서의 split 이랑 좀 다르다!!!

print(arr1_split)