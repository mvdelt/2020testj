a = ['a','b','c']

def testj():
    # global a
    a2 = a # i. 이렇게하면 a2 는 a 를 가리킴. 즉, global a 를 하지 않더라도 a2가 전역변수 a 랑 같은놈이 됨.
    a2.append('i am a2')
    print('a2:',a2)

testj()
print('a:',a) # i. 요놈이 바뀐것을 확인할수있음.