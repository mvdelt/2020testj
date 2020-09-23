import torch

class Jnet(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(10,5)
        self.l2 = torch.nn.Linear(5,3)
        self.relu = torch.nn.ReLU()
    def forward(self, x):
        x = self.l1(x)
        x = self.l2(x)
        x = self.relu(x)
        return x

jnet = Jnet()
print(f'jnet.l2: {jnet.l2}')
print(f'jnet.parameters(): {jnet.parameters()}')
inTensor_ex = torch.tensor([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.11])
outputj = jnet(inTensor_ex)

print(f'outputj: {outputj}')

print(f'jnet.parameters(): {jnet.parameters()}')

pgen = jnet.parameters()
pgen_iter = iter(pgen)
print(next(pgen_iter))
print(next(pgen_iter))
print(next(pgen_iter))
print(next(pgen_iter))
print(next(pgen_iter))