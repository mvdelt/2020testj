import torch

t1 = torch.tensor([11,22,33,44,33,55,66])
t2 = torch.tensor(111)

T1 = torch.Tensor([2,3,4,5])
T2 = torch.Tensor(22)


# print(t1)
# print(t2)

# print(T1)
# print(T2)

t1_eq = (33 == t1)
print(t1_eq)
t1_eq_nz = (t1 == 33).nonzero()
print(t1_eq_nz)
t1_eq_nz_sq = (t1 == 33).nonzero().squeeze()
print(t1_eq_nz_sq)
print('t1 selected:',t1[t1_eq_nz_sq])

z1 = torch.zeros( (3,4,5,6) )
print(z1)
idx_tensor = torch.tensor([1,2])
print(z1[idx_tensor])
