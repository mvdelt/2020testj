import torch

# tensor1 = torch.randn(2,3,4)
# print(tensor1)

# # tensor2 = torch.randn(2,3,2)
# # print(tensor2)

# tensor3 = torch.tensor([100,200])
# print(tensor3)

# # i. 복사. detach()는 계산그래프에서 디태치시키는역할인가봄. - 파이토치의 텐서를 복사하는방법은 여러가지가 있는듯함. 일단 요렇게 해줘봄. 잘 작동하는듯.
# tensor1add3 = tensor1.clone().detach() 

# # i. in place 로 tensor1add3 의 선택된(인덱싱해준)부분에 tensor3 을 더해줌.(in place, 즉, tensor1add3 이 바뀜.)
# # 이때, broadcast 됨을 확인할수있음. numpy 의 broadcast 기능처럼.
# tensor1add3[:,:,:2] += tensor3 

# # print(tensor1+tensor3) # RuntimeError: The size of tensor a (4) must match the size of tensor b (2) at non-singleton dimension 2
# print(tensor1add3)
# print(tensor1) # i. 얜 그대로 있음.

# # tensor1[:,:,:2] += tensor2
# # print(tensor1)

#####################################

# t1 = torch.tensor([1,2,3])
# t2 = torch.tensor([[1,2,3]])
# t1_2 = torch.tensor([t1]) # ValueError: only one element tensors can be converted to Python scalars

# print(t1)
# print(t2)
# print(t1.shape)
# print(t2.shape)
# print('t1_2:',t1_2)


# a = torch.tensor([[0,1,2],[3,4,5],[6,7,8]])
# print(a)
# print(a.shape) # i. (3,3) 으로 나오겟지.
# # a2 = a.unsqueeze(0)
# # print(a)
# # print(a2)
# # a.unsqueeze_(-1) # i. -1 의 의미는 마지막 축(axis) 을 의미하는거겟지. 해보니 그렇고.
# a.unsqueeze_(2) # i. 즉, 여기서의 a의 경우, a.unsqueeze(-1)은 a.unsqueeze(2) 와 같은거지. - 참고로 언더스코어 잇고없고는 in place 로 해주냐 마냐 차이임. 
# # i. 즉, T.unsqueeze_(N) 이라고 하면, T라는 텐서의 쉐입에서 N번째 축(0부터 카운트)을 1로 만들어주면서 쉐입의 원소갯수(축 갯수)를 1개 더 늘려주게 되는듯함(축을 하나 더 늘림).
# print(a)
# print(a.shape) # i. (3,3,1) 로 나오겟지.
# a = a.expand(3,3,10)
# print(a)
# print(a.shape) # 3,3,10

###########################################

# z = torch.tensor(880)
# print(z)
# print(z.shape)
# print(len(z))

tt = torch.tensor([22, 33])
tt2 = tt[0]
tt3 = tt[0:1]
print(tt2) # tensor(22)
print(tt3) # tensor([22])
# print(len(tt2)) # TypeError: len() of a 0-d tensor
print(len(tt3)) # 1
