# i. 2020.08.19.수욜오전.) 릿코드 3sum 문제 내풀이. 시간초과해서 억셉되진 않앗지만, 매우 맘에 듦!
# 왜냐면, DP방식 사용해서 3개뿐 아니라 일반적인 n개에 대해서 풀수있기 때문! 
# 근데 사람들이 올린 O(n^2)time 솔루션들 보니까, 매우 좋긴 함!!

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def inner(tar, num, nums):
        
            # i. boundary condition.
            if num==1:
                return {(n,) for n in nums if tar==n}
        
            tup_set = set()
            for n in nums:
                nums_wo_n = nums[:]
                nums_wo_n.remove(n)
                tupset = inner(tar-n,num-1,nums_wo_n)
                for tup in tupset:
                    li = list(tup)
                    li.append(n)
                    li.sort()
                    tup_set.add(tuple(li))
            return tup_set
        
        return inner(0, 5, nums) # i. 요기서 갯수를 맘대로 바꿔도 잘 작동한다는거지!

sol = Solution()
nums=[1,3,-2,-5,3,7,8,-1,2,3,4,-3,-2]
ret = sol.threeSum(nums)
print(ret)