"""
 House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that 
adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
"""



class Solution:
    def profit(self,i,n,nums):
        if i>n:
            return 0
        return nums[i]+max(self.profit(i+2,n,nums), self.profit(i+3,n,nums))
    def rob(self, nums: List[int]) -> int:
        return max(self.profit(0,len(nums)-1,nums), self.profit(1,len(nums)-1,nums))


# -> Submission Result: Time Limit Exceeded



# i. 아래처럼 하니까(memoization 하려고 한건데, 잘 됏나 몰겟네) 일단 accept 됨!!

class Solution:
    def profit(self,i,n,nums):
        if i>n:
            return 0
        if self.memo[i]!=None:
            return self.memo[i]
        self.memo[i] = nums[i]+max(self.profit(i+2,n,nums), self.profit(i+3,n,nums))
        return self.memo[i]
    def rob(self, nums: List[int]) -> int:
        self.memo = [None]*len(nums)
        return max(self.profit(0,len(nums)-1,nums), self.profit(1,len(nums)-1,nums))
