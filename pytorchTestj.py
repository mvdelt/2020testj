from __future__ import print_function
import torch


tt0 = torch.tensor([[2,4,6],[1,2,3]])
tt = torch.tensor([10,20]) # i. torch.tensor(5)는 그냥 torch.tensor([5])랑 똑같은듯. 걍 원소 1개짜리 텐서인듯.
print('tt:',tt)
# prd = tt0 * tt
# print('tt0 * tt :',prd)
added = sum(tt0,tt)
print('tt0 + tt :', added)

x = torch.empty(5, 3)
print('x:',x)

# x = x.new_ones(5, 6, dtype=torch.float)      # new_* methods take in sizes
# print(x)

# x = torch.ones_like(x, dtype=torch.double)    # override dtype!
# print(x)  



# let us run this cell only if CUDA is available
# We will use ``torch.device`` objects to move tensors in and out of GPU
if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    print('torch.device(\'cuda\'):',device)
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    x = x.to(device)                       # or just use strings ``.to("cuda")``
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))       # ``.to`` can also change dtype together!

else: 
    print('cuda not availabe j!')