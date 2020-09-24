import torch

t = torch.tensor([334])
t2 = torch.tensor(334)
t3 = torch.tensor([334, 447])
t4 = torch.tensor([[334, 447],[1,2],[5,6]])

print(t)
print(t2)
print(t3)

print(t.item())
print(t2.item())
# print(t3.item()) # ValueError: only one element tensors can be converted to Python scalars

print(t.size())
print(t2.size())
print(t3.size())
print(t4.size())