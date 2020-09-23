import torch

a = torch.randn(3, 3, requires_grad=True)
print(f'a:{a}')

b = a+torch.tensor(2)
print(f'b:{b}')
print(f'is b a leaf?: {b.is_leaf}') # False


b2 = b.detach()
print(f'is b2 a leaf?: {b2.is_leaf}') # True
print()


a2 = a.detach()
print(f'is a2 a leaf?: {a2.is_leaf}')

a2 = a.detach().clone()
print(f'a2:{a2}')

a2 += torch.tensor(1)
print(f'a2:{a2}')
print(a2.requires_grad)
print(f'a:{a}')
print(a.requires_grad)