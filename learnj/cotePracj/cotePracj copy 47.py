'''
# i. 2020.08.27.) 백준 '트리인가?' 문제.
'''

# 콘솔입력받기. 빡시네;;
hubos = []
while True:
    hubo=[]
    while True:
        line = input()
        if line=='':
            continue
        if line[-2]=='-':
            break
        if line[-1]=='0':
            hubo+=line.split()[:-2]
            break
        else:
            hubo+=line.split()
    if line[-2]=='-':
        break
    hubos+=[hubo]
print(f'hubos:{hubos}')

# 트리후보리스트를 받아 결과리스트 리턴하는 함수.
def checkIfTreej(hubos):
    flags = [True]*len(hubos)
    for hubodx, hubo in enumerate(hubos):
        # 텅빈것도 트리로 친다함.
        if len(hubo)==0: continue


        from collections import defaultdict
        vmap = defaultdict(list)
        for u,v in zip(hubo[::2], hubo[1::2]):
            vmap[v]+=[u]
        
        # 이제 tree가 맞는지 확인.
        ## 1. 들어오는 간선이 하나도 없는 단 하나의 노드가 존재한다. 이를 루트(root) 노드라고 부른다.
        ### root 1개인지 체크, 1개면 변수바인딩해놓음.
        if len(vmap)+1 != len(set(hubo)):
            flags[hubodx] = False; continue
        root = next(iter(set(hubo)-set(vmap.keys())))

        ## 2. 루트 노드를 제외한 모든 노드는 반드시 단 하나의 들어오는 간선이 존재한다.
        for (v,uli) in vmap.items():
            if len(uli)!=1: flags[hubodx]=False; continue

        ## 3. 루트에서 다른 노드로 가는 경로는 반드시 가능.
        for v in vmap:
            count=0
            while v in vmap and count<=len(set(hubo))-1:
                count+=1
                v = vmap[v][0]
            if count==len(set(hubo)) or v!=root:
                flags[hubodx] = False; continue       
    return flags

# 함수 실행.
flags = checkIfTreej(hubos)

# 각 후보에대한 결과 출력.
for fdx, flag in enumerate(flags): 
    if flag:
        print(f'Case {fdx+1} is a tree.')
    else:
        print(f'Case {fdx+1} is not a tree.')
