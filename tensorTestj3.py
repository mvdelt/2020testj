# import torch

# t1 = torch.randn(5, 3, 2)
# t2 = torch.tensor([1,3])

# print(t1)
# print(t2)

# print(t1.shape)

# print(t1[t2,1])
# print(t1[t2,1].shape)

######################################
import torch
t1 = torch.randn(3,4,5)
print(t1.size()) # torch.Size([3, 4, 5])
print(t1.size()[0]) # 3
print(t1.shape) # torch.Size([3, 4, 5]) -> i. .size()가 원래 있었는데, 넘파이랑 비슷하게 맞춰주려고 .shape 이라는걸 추가했다고 봤음. 기능은 둘다 똑같다는듯.
print(t1)