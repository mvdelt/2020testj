"""
LeetCode '4sum II' 하드급문제.
디자인: 
구현: 
"""

from typing import List
class Solution:
    def __init__(self):
        self.memo={}

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # self.ABCD = [A,B,C,D]

        return self.helper(0, [A,B,C,D])
    
    def helper(self, sumj, li):
        
        if len(li)==1:
            return li[0].count(sumj)

        # i. 위의 if 대신 이렇게해도 잘 작동하긴 하는듯.
        # if li==[]:            
        #     if sumj==0: return 1
        #     else: return 0

        if (sumj, len(li)) in self.memo:
            return self.memo[(sumj, len(li))]

        first = li[0]
        cnt=0
        for num in first:                            
            cnt+=self.helper(sumj-num, li[1:])

        self.memo[(sumj, len(li))] = cnt
        
        return cnt

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

sol=Solution()
ret = sol.fourSumCount(A,B,C,D)
print(ret)