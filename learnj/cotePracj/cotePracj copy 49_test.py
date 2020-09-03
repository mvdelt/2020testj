"""
2020.08.30.일욜아침. Python으로 콘솔입력받는거 테스트.
"""
import sys

# line = sys.stdin.readline()
# print(line)
# print(type(line))

lines = sys.stdin.readlines()
print(lines)
print(type(lines))
print([line.rstrip('\n') for line in lines])
print([line.rstrip() for line in lines])
print([line.strip() for line in lines])

# buf = sys.stdin.read()
# print(f'buf:{buf}')
# print(f'type(buf):{type(buf)}')
# print(f'buf.split():{buf.split()}')

# print(sys.stdin)
# triangle = [list(map(int, s.rstrip().split())) for s in sys.stdin.readlines()]
# print(triangle)


# i. 아래는 백준 다른사람 풀이인데, sys.stdin.readlines() 가, 사용자가 EOF신호(ctrl+d, 윈도에선 ctrl+z) 입력하기전까진 계속 입력을 받는데, 백준에서 통과되네;;
# 백준에서 입력다마쳣으면 EOF 신호 보내나봄.
# 참고로 strip() 은 스트링의 양쪽 다 스트립핑 하는거, rstrip()은 오른쪽 여백(스트링의 맨 끝에있는)만 스트립핑, rstrip('\n') 는 뉴라인캐릭터만 제거.

# import sys
# height = int(sys.stdin.readline().rstrip())
# triangle = [list(map(int, s.rstrip().split())) for s in sys.stdin.readlines()]

# for h in range(1, height):
#     for i, num in enumerate(triangle[h]):
#         if i==0: triangle[h][i] += triangle[h-1][0]
#         elif i==len(triangle[h])-1 : triangle[h][i] += triangle[h-1][-1]
#         else: triangle[h][i] += max(triangle[h-1][i-1], triangle[h-1][i])

# print(max(triangle[-1]))