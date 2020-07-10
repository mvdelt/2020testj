import numpy as np
import random

a = np.random.uniform(-10, 30)
print(a)
a = np.random.uniform(-10, 30, 5)
print(a)
a = np.random.uniform(-10, 30, (2,3))
print(a)
a = np.random.uniform(-10, 30, (2,3)).mean()
print(a)

r = random.Random(42) # i. 인풋인자로 들어가는 값은 seed 임.
print(set(range(10)))
rs = r.sample(set(range(10)),k=5)
print(rs)