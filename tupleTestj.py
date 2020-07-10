tu1 = (1,3,5)
for i in tu1:
    print(i.__class__.__name__)

li1 = [1,2,3,   4,5,6,   7,8,9,   10,11,12,   13,14,15,   16,17,18]

j = 1

print([li1[3*j:3*j+3] for j in tu1])

############################################# 아래는 다른거 테스트.
aaa = tuple(512 for _ in range(8))
print("aaa:",aaa)