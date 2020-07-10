inputStr = "[2,3,4,5]"
print(map(float, inputStr.strip('[]').split(',')))
# [2.0, 3.0, 4.0, 5.0] # i. 파이썬3에선 map 객체가 출력됨.
A = map(float, inputStr.strip('[]').split(','))
print(A, type(A))
# ([2.0, 3.0, 4.0, 5.0], <type 'list'>) # i. 이건 파이썬2 에서의 결과인가봄. 3에선 다름.

Ali = list(A) # i. 이렇게하면 파이썬3에서도 의도한결과 출력가능.
print(Ali, type(Ali))