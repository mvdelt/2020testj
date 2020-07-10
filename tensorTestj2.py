import torch

t1 = torch.randn(3, 4, 5)

print(t1)
# print(t1.max(0)) # i. 어떤축에서 max를 고를지 선택가능. 이렇게 0을 넣으면, 축 0 으로 max값들 고르고, 인덱스도 보여주네.
print(t1.max()) # i. 이건 걍 모든 원소들중 max값 골라냄. 
print(round(float(t1.max()),2))