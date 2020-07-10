# losses = sum(loss for loss in loss_dict.values())


dict1 = dict(j=3, hi=100, namej = 5, agej=888)
print('dict1:',dict1)

print('dict1.values():',dict1.values())

vs = sum(v for v in dict1.values())
print(vs)

# print(v for v in dict1.values())