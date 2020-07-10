import numpy as np

arr1 = np.random.randint(10, size=(5, 2, 3))
mularr = np.arange(10).reshape(5,2,1)
print('arr1:',arr1)
print('mularr:',mularr)
print('arr1*mularr:',arr1*(1-mularr))
