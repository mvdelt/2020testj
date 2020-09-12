
a='hi'
b='kk'
c=None
d='jun'
e='eee'
f=''

print(a and b and c and d) # None
print(a and b and c and d or e) # 'eee'
print(a and b and c and d or e and f) # ''
print(a and b and c and d or e and f or 'haha') # 'haha'  # i. 왼쪽에서부터 오른쪽 방향으로 순차적으로 연산된다고 보면 되네.
print('j) 추가테스트:',True or False and False) # i. -> 아니다!!!!!! 순차적이 아니고, 'or' 보다 'and' 가 더 우선된다!!!!!
print('j) 추가테스트2:', True or False and False or False and False and False or False and False) # True
# i. ->즉 True 뒤에 or 가 나오면, 그뒤에 뭐가 잔뜩 줄줄이 있든간에 그 True 가 결괏값이 되는거!!!
# 중요한거: 연산자의 우선순위와, 실행순서는 다른 개념!!!
# 연산자의 우선순위는 '괄호'가 쳐지는 방식이라고 보면 됨. 예를들어 수학에서 A + B x C 는 A + (B x C) 인것처럼.
# 하지만 실행은 왼쪽->오른쪽 순서대로임!!!
# 스택오버플로 개굿: https://stackoverflow.com/questions/51784005/python-or-and-operator-precedence-example

def some_fct_j(a):
    # i. some codes..

    truthy_or_falsy = a
    some_meaningful_valuej = 'I am gonna be returned!!'

    # i. return A and B or C 구문(?)ㅋㅋ.
    # 지금과같이, some_meaningful_valuej 가 truthy 하다는 전제하에,
    # 1) truthy_or_falsy 가 truthy 한 값이면, some_meaningful_valuej 가 리턴될것이고,
    # 2) truthy_or_falsy 가 falsy 한 값이면, 'some_default_valuej' 가 리턴될것임.
    return truthy_or_falsy and some_meaningful_valuej or 'some_default_valuej'
            
print(some_fct_j('yeah'))
print(some_fct_j(''))

