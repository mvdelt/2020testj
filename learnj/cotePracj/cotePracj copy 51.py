"""
LeetCode 'Search for a range' 미디엄급문제.
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ans = []

        # i. finding left limit.
        rdx = len(nums)-1
        ldx = 0
        while ldx<rdx:
            mdx = (ldx+rdx)//2
            if target <= nums[mdx]:
                rdx = mdx
            elif nums[mdx] < target:
                ldx = mdx+1                
        if ldx < len(nums) and nums[ldx]==target:
            ans+=[ldx]
        else:
            return [-1,-1]
            
        # i. finding right limit. don't ldx=0 cuz it's been found above.
        rdx = len(nums)-1
        while ldx<rdx:
            import math
            mdx = math.ceil((ldx+rdx)/2)
            if target < nums[mdx]:
                rdx = mdx-1
            elif nums[mdx] <= target:
                ldx = mdx
        ans+=[ldx]

        return ans

nums_ex, target_ex = [5,7,7,8,8,10], 8
sol=Solution()
ret=sol.searchRange(nums_ex, target_ex)
print(ret)