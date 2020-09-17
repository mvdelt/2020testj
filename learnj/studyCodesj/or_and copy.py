import torch, math

# print(range(64)) # range(0, 64)
# print(type(range(64))) # <class 'range'>

tt = torch.tensor([[1,2],[3,4],[5,6]])
target = torch.tensor([[0,0,0],[1,1,1]])
# print(tt)
print(tt[range(3)])
# print(tt[range(2), 0])
# print(tt[range(2), 1])

print(tt[range(3), target])

# b = torch.arange(4 * 5 * 6).view(4, 5, 6)
# print(b)
# b2 = b.view(6,20)
# print(b2)
# b2[5,0]=4444
# print(b)
# print(b2)

# c = torch.arange(2 * 3 * 4).view(2, 3, 4)
# print(c)
# print(torch.sum(c, -1))
# print(torch.sum(c, 1))
# print(torch.sum(c, (2, 1)))
e = math.e
d = torch.tensor([[0.1,0.2],[0.3,e]])
print(d)
print(d.exp())
# print(d.log())


print('--------------')

def log_softmax(x):
    return x - x.exp().sum(-1).log().unsqueeze(-1)

print(d.exp().sum(-1))
print(d.exp().sum(-1).log())
print(d.exp().sum(-1).log().unsqueeze(-1))
print(log_softmax(d))

print(d==torch.tensor([0.1,0.3]).unsqueeze(-1))
print(torch.tensor([0.1,0.3]).unsqueeze(-1))