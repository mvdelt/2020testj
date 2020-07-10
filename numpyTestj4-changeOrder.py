import numpy as np

a = np.arange(1,13).reshape(2,2,3)
print(a)

b = a[:,:,[0,2,1]]
print(b)