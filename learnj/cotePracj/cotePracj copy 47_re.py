'''
# i. 2020.08.27.) 백준 '트리인가?' 문제.
    다른사람풀이 테스트중.
    -> ㅡㅡ; 백준 테스트시스템 틀렸다!!!
     예를들어 1->2, 3->4, 4->5, 5->3 이런식으로 cyclic 한 노드들이 분리되어 있으면, 
     얘는 문제의 트리 조건 3번에 안맞는데(root에서 모든 노드들에 접근가능해야함),
     지금 요 풀이는 트리라고 출력한다.
     근데 통과한 풀이다;;;
'''

# import sys
# print('j_ this is test')
# print('   a  b c def    gh    \n   hihi  d \n')
# print('   a  b c def    gh    \n   hihi  d \n'.split())
# buf = sys.stdin.read()
# print(buf.split())


# 다른사람의 풀이. 단지 노드갯수-1 == 엣지갯수 인지만 판단한다;; 근데 백준 통과;; 위에서 적은 반례도 트리라고 하는데도 통과;; 
# import sys
# buf = sys.stdin.read()
# buf = list(map(int, buf.split()))
# print(buf)
# k = 0
# nodes = []
# linecnt = 0
# while True:
#     u = buf.pop(0)
#     v = buf.pop(0)

#     if u == -1:
#         break
#     if u == 0 and v == 0:
#         k += 1
#         nodes = list(set(nodes))
#         if len(nodes) == 0 or len(nodes)-1 == linecnt:
#             print(f'Case {k} is a tree.')
#         else:
#             print(f'Case {k} is not a tree.')
#         nodes.clear()
#         linecnt = 0
#     else:
#         linecnt += 1
#         nodes.append(u)
#         nodes.append(v)