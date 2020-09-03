'''
# i. 2020.08.24.) 백준 '친구' 문제.
<친구> 
문제
지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다. 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다. 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.
A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.
입력
첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다. (예제를 참고)
출력
첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.
'''

# i. 내 풀이. 억셉됏음.
from collections import defaultdict
N = int(input())
fdict = {}
for i in range(N):
    fdict[i] = [jdx for jdx, j in enumerate(input())if j=='Y']

f2dict= defaultdict(list)
for p, fs in fdict.items():
    for f1 in fs:
        f2dict[p] += fdict[f1]
    if not fs: # i. fs 리스트가 텅비었을땐 위의 for문이 수행되지 않기때문에 여기서 이렇게해줌.
        f2dict[p] = []

# i. -{p} 를 해주는이유: 자기자신은 2-친구 에 포함되지않아야하기때문에 자기자신은 빼줌.
numf2_set = {len(set(fs+f2s)-{p}) for p, fs, f2s in zip(fdict.keys(), fdict.values(), f2dict.values())}
print(max(numf2_set))



