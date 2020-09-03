from typing import List # i. generic 하게 하려면 이걸임포트해줘야하네.

class Solution:
    def removeDuplicates(self, nums: List[int])->int:
        
        numset = set(nums)
        for n in numset:
            nc = nums.count(n)
            for _ in range(nc-1):
                nums.remove(n)        
        return len(nums)
        
sol = Solution()
nums_ex = [1,1,2,3,3,3,4,5,5,5,5,6,6,7]
ret=sol.removeDuplicates(nums_ex)
print('nums_ex:',nums_ex)
print('ret:',ret)

# i. 흠. ....계속뭔가잘못하고잇다. leetcode "Remove Duplicates from Sorted Array" 문제임.
# for문돌릴때 뭔가 리스트 원소 삭제되면서 순서대로안되고 좀 엉키는것때문이아닌가싶은데..일단자자.
# ->담날해결.