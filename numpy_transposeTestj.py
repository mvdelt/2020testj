import numpy as np

a = np.arange(1,13).reshape(2,2,3)
print(a)

a_T = a.transpose(2,0,1)
print(a_T)

# i. ㅇㅋ 이해완료!