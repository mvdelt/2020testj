import numpy as np

li = [0,1,2,3,4,5,6,7,8]
arr = np.array(li)
print(arr)
print(arr[0::3]) # i. [0,3,6] 이겟지.
print(arr[0::3]**2-1)
print(arr)
arr[0:3]+1
print(arr[0:3]+10)
print(arr)
