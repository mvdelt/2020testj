li = [1,2,3,4,5,6,7,8,9,10,33,44,55,66,77,21,22,23,24,51,56,57,58,59,60]

# i. key 를 이용한 정렬. 
# li.sort(key=lambda x: (-(x%2), -x if x%2==0 else x)) # i. 이렇게 해도 됨!
# li.sort(key=lambda n: (n % 2 == 0, (n % 2 and 1 or -1) * n))  # 이렇게해도 되고. and가 or 보다 더 우선적으로 연산되나봄.

# i. cmp 를 이용한 정렬.(functools.cmp_to_key 를 이용). cmpf함수는 내가만들어본것임.
def cmpf(a,b):
    if a%2 != b%2:
        if a%2 == 0:
            return 1
        else:
            return -1
    else:
        if a%2 == 0:
            return b-a
        else:
            return a-b
from functools import cmp_to_key
li.sort(key=cmp_to_key(cmpf))



print(li)

print(10 % 2 and 1)
print(11 % 2 and 123)
print(False or -1)
print(True or -1)
print(10 % 2 and 1 or -1)
# print(1 or -1)
# print(7 or -5)
# print(0 or -1)
# print(0 or -3)
# print(43 or 0)