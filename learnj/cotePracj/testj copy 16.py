from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ret = []        
        for idx, i in enumerate(nums):
            for k in (nums+nums)[idx+1:idx+len(nums)]:
                if k>i:
                    ret.append(k)
                    break
            else:
                ret.append(-1)
        return ret

sol = Solution()
nums=[1,2,1]
ret= sol.nextGreaterElements(nums)
print(ret)