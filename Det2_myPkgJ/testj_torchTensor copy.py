import torch

t = torch.randn(2,3) # Initially dtype=float32, device=cpu

print(t)
print(type(t))
# print(t.double())
# print(type(t))
print(t.to(torch.float64)) # self.double() is equivalent to self.to(torch.float64). See to().
print(type(t))
