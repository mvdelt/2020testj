"""
LeetCode 'Spiral Matrix' 하드급문제.
디자인: 쉬웠음. 좀 이것저것 생각하다 최종 슈도코드 작성까지 20분걸림.
구현: 얼추20분정도걸렸고 완성해서 테스트까지해보니 28분. 
총시간 48분쯤 걸림.
"""
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # i. idea: 포인터가 spiral하게 이동, 원소값을 읽어서 out 리스트에 담음.
        # 포인터가 방문했던곳은 원 maxtrix 에 in place 로 '#'을 덮어씌워서 표기.

        if matrix==[]: return [] # i. 가로세로길이 모두 0인 matrix가 주어질경우.

        out = []
        out+=[matrix[0][0]]
        matrix[0][0]='#'
        r,c=0,0

        # while not (읽어들인갯수 == matrix원소갯수)
        while not len(out)==len(matrix)*len(matrix[0]):
            
            # while not (오른쪽 원소가 없다 or 이미갔던원소다):
            while not (len(matrix[0])==c+1 or matrix[r][c+1]=='#'): # i. 인덱스범위벗어난오류가능? -> 오류 안난다!!!!!!
            # -> or로 연결됏을때 그전에 truthy가 나오면 그뒤엣놈은 아예 실행 안하나봄!!

                # 오른쪽이동.
                c+=1
                # 읽어서 out에 담음.
                out+=[matrix[r][c]]
                # 원 매트리스의 해당원소를 '#'로 덮어씌움.
                matrix[r][c]='#'
            
            # 이 while문을 아래,왼쪽,위 도 똑같이 반복.

            # while not (아래 원소가 없다 or 이미갔던원소다):
            while not (len(matrix)==r+1 or matrix[r+1][c]=='#'): # i. 인덱스범위벗어난오류가능?
                # 아래이동.
                r+=1
                # 읽어서 out에 담음.
                out+=[matrix[r][c]]
                # 원 매트리스의 해당원소를 '#'로 덮어씌움.
                matrix[r][c]='#'

            # while not (왼쪽 원소가 없다 or 이미갔던원소다):
            while not (c==0 or matrix[r][c-1]=='#'): # i. 인덱스범위벗어난오류가능?
                # 왼쪽이동.
                c-=1
                # 읽어서 out에 담음.
                out+=[matrix[r][c]]
                # 원 매트리스의 해당원소를 '#'로 덮어씌움.
                matrix[r][c]='#'

            # while not (위 원소가 없다 or 이미갔던원소다): ->'위 원소가 없다'여부 체크해야할까? 일단체크. 
            while not (r==0 or matrix[r-1][c]=='#'): # i. 인덱스범위벗어난오류가능?
                # 위이동.
                r-=1
                # 읽어서 out에 담음.
                out+=[matrix[r][c]]
                # 원 매트리스의 해당원소를 '#'로 덮어씌움.
                matrix[r][c]='#'

        return out


mat_ex=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
mat_ex=[
    [1]
]
mat_ex=[
    [1,3],
    [5,7]
]
mat_ex=[
    [1,3,5,7],
    [9,11,13,15]
]
mat_ex=[
    [1,3],
    [9,11],
    [4,5]
]
mat_ex=[
    [1],
    [9],
    [4]
]
mat_ex=[
    [1,3,5,7]
]
mat_ex=[] # i. 이걸빠트렸네;;
mat_ex=[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]

sol = Solution()
ret=sol.spiralOrder(mat_ex)
print(ret)