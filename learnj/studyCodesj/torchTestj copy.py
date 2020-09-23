import torch

a = torch.tensor([1,2,3.], requires_grad = True)
out = a.sigmoid()
c = out.detach()
czero = c.zero_()
print(f'czero: {czero}')  # tensor([ 0.,  0.,  0.])


print(f'out: {out}')  # tensor([ 0.,  0.,  0.])  # ->modified by c.zero_() !!


out.sum().backward()  # Requires the original value of out, but that was overwritten by c.zero_()
# RuntimeError: one of the variables needed for gradient computation has been modified by an inplace operation: ...(생략)