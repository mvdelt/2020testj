'''
# i. 2020.08.27.) 백준 '트리인가?' 문제. ->백준 콘솔입력을 어케준다는건지 애매해서 다시. 각 후보들마다 출력값 리턴하는건가봄;;
 -> 계속 런타임에러뜸;;;
'''


def checkIfTreej(hubo):
    from collections import defaultdict
    vmap = defaultdict(list)
    for u,v in zip(hubo[::2], hubo[1::2]):
        vmap[v]+=[u]
    
    # 이제 tree가 맞는지 확인.
    ## 1. 들어오는 간선이 하나도 없는 단 하나의 노드가 존재한다. 이를 루트(root) 노드라고 부른다.
    ### root 1개인지 체크, 1개면 변수바인딩해놓음.
    if len(vmap)+1 != len(set(hubo)):
        return False
    root = next(iter(set(hubo)-set(vmap.keys())))

    ## 2. 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다.
    for (v,uli) in vmap.items():
        if len(uli)!=1: return False

    ## 3. 루트에서 다른 노드로 가는 경로는 반드시 가능.
    for v in vmap:
        count=0
        while v in vmap and count<=len(set(hubo))-1:
            count+=1
            v = vmap[v][0]
        if count==len(set(hubo)) or v!=root:
            return False
    return True


hubodx=0
hubo=[]
while True:
    fg=False
    line=input()
    if line[-2]=='-':
        hubo+=line.split()[:-4]; fg=True  
        
    # if line[-1]!='0':
    #     hubo+=line.split()
    #     continue
    else:
        hubo+=line.split()[:-2]

    hubodx+=1
    if checkIfTreej(hubo):
        print('Case {} is a tree.'.format(hubodx))
    else:
        print('Case {} is not a tree.'.format(hubodx))
    hubo=[]
    if fg: break



# # 각 후보에대한 결과 출력.
# for fdx, flag in enumerate(flags): 
#     if flag:
#         print(f'Case {fdx+1} is a tree.')
#     else:
#         print(f'Case {fdx+1} is not a tree.')



# 3 8  6 8  6 4  5 3  5 6  5 2  0 0  -1 -1
# 8 1  7 3  6 2  8 9  7 5  7 4  7 8  7 6  0 0