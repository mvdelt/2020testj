li = [1,2,3,4,5,6,7,8]

while not(len(li)==20):
    li.append(li[-1]+1)
    if len(li)==19:
        li.append(20)
        if len(li)==20:
            print('len(li)==20')
        break

else:
    print('hh')


print(li)


# i. 파이썬에서 while-else 구조, for-else 구조 이해완료. break 가 있을때만 요 else를 쓰는 의미가 있음(break안쓰면 else도 쓸필요없음).
# break는 while또는for 루프만 탈출하는게 아니라, while또는for 과 연결되는 else까지도 탈출함. 
# while또는for - else 구조에서 else는 "if not break" 라는 의미로 생각해도 됨.