'''
# i. 2020.08.25.) 백준 '트리 순회' 문제. 통과완료.
입력
첫째 줄에는 이진 트리의 노드의 개수 N(1≤N≤26)이 주어진다. 
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 
노드의 이름은 A부터 차례대로 영문자 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 
자식 노드가 없는 경우에는 .으로 표현된다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 
각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
'''
class Node:
    def __init__(self, nm=None, ln=None, rn=None):
        self.nm = nm
        self.ln = ln
        self.rn = rn

N = int(input())
nm2node = {} # i. nm은 name의 줄임말.
for _ in range(N):
    (root_nm, ln_nm, rn_nm) = tuple(input().split())
    
    if root_nm in nm2node:
        root_node = nm2node[root_nm]
    else:
        root_node = Node(root_nm)
        nm2node[root_nm] = root_node

    ln = Node(ln_nm)
    rn = Node(rn_nm)
    root_node.ln = ln
    root_node.rn = rn
    nm2node[ln_nm] = ln
    nm2node[rn_nm] = rn

# for k,v in nm2node.items():
#     print(f'k:{k}, v.nm:{v.nm}')
# print(nm2node['a'].ln.ln.nm)


# i. 전위순회
def pre(root):
    if root.nm == '.':
        return ''
    return root.nm + pre(root.ln) + pre(root.rn)
print(pre(nm2node['A']))

# i. 중위순회
def inord(root):
    if root.nm == '.':
        return ''
    return inord(root.ln) + root.nm + inord(root.rn)
print(inord(nm2node['A']))

# i. 후위순회
def post(root):
    if root.nm == '.':
        return ''
    return post(root.ln) + post(root.rn) + root.nm
print(post(nm2node['A']))
    

