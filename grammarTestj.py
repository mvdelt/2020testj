l1 = [3,4,5,6,7,8,9,10,11,12,13,14]

# i. 당연히, 이건 작동 됨.
# for i in l1:
#     if i%2==0:
#         print(i)


# i. 근데, 이건 작동 안됨!!!
# for i in l1 if i%2==0: 
#     print(i)

# i. 근데, list comprehension 에서는 요렇게 해도 됨!!!
li2 = [i for i in l1 if i%2==0]
print(li2)