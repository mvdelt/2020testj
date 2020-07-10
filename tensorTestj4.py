import torch

t1 = torch.randn(5,3)
print(t1)

l1 = [2,0,3]

# i. 아래 코드가 어케동작하나 테스트하기위함. num_objects_per_image_list 의 원소중에 0이 있을때 어케되나 보려고. -> 상식적으로 됨.
# pred_kp_logits_splited = pred_kp_logits.split(num_objects_per_image_list, dim=0)

t2 = t1.split(l1, dim=0) # i. 참고로, 넘파이의 split 이랑은 좀 다름!! 

for i in t2:
    print(i)
    print(i.size())