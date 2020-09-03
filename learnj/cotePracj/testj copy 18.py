
# n=13424
# print(list(str(n)))

# print(set(str(888775555)))
# print(list(set(str(888775555)))[0])

# print(min([4,6,8,10]))

# numberj=55
# N=5
# print(len(set(str(numberj))))
# print(list(set(str(numberj))))
# if len(set(str(numberj)))==1 and list(set(str(numberj)))[0]==str(N):
#     print('j) 이어붙이기!!')



import copy
li = [[0]] # i. 첨엔 리스트 원소갯수가 1개뿐.
mon = [3,5,7,8,4]
for i in li: # i. for문에서 리스트 원소갯수를 늘리고있음. 잘 됨!!
    for d in range(2,4):
        if sum(i) > (len(mon)-1):  # sum(i): 마지막인덱스값(len-1)과 동일.
            continue
        i_copy = copy.deepcopy(i) # 딥카피 해줘야 내의도대로됨!!
        i_copy.append(d)
        li.append(i_copy)
        # i.append(d)
        # li.append(i)
        # print(li)

print(li) # i. for문에 의해서 리스트 원소들이 엄청 늘어났음.