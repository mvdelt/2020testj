
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

