"""
LeetCode '4sum II' 하드급문제. 2번째 풀이. 내가생각한거아니고, 릿코드 디스커션 보고 아이디어 캐치 후 구현만 해보는것.
디자인: 
구현: 
"""

# i. 이 풀이의 핵심: 쪼개서 for문 돌리기!!!
# 그냥 for loop 을 4번 돌리면 time complexity 가 O(N^4) 가 되지만,
# 두개 두개씩 쪼개서 for문 2번돌리는것을 두번 함으로써 O(N^2)+O(N^2) -> O(N^2) 의 시간복잡도가 됨!! 


from typing import List
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = {}
        for a in A:
            for b in B:
                if a+b in AB: AB[a+b]+=1
                else: AB[a+b]=1
        cnt=0
        for c in C:
            for d in D:
                if -c-d in AB: cnt+=AB[-c-d]
        return cnt

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

sol=Solution()
ret = sol.fourSumCount(A,B,C,D)
print(ret)