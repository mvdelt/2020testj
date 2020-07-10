# import math
# import numpy as np

# center1 = (10,50)
# center2 = (13,54)
# # i. 그냥 파이썬 튜플끼리 빼면 에러나네. 어쩔수없이 넘파이 사용해줘봣음(결과는 어레이로 나옴). 튜플의 각 원소끼리 빼도되지만 그럼좀지저분해지니 다른방법 써본거임.
# dist = math.sqrt(sum(np.subtract(center1,center2)**2))

# print(dist)
# print(dist.__class__)

# # sum_center2 = sum(center2)
# # print(sum_center2)

############################################

value_list = [3,6,5,77,1,99]
index_min = min(range(len(value_list)), key=value_list.__getitem__)
print(range(len(value_list)))
print(value_list.__getitem__(3))
print(index_min)
