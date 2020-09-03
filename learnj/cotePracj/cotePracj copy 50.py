"""
LeetCode 'Jump Game' 미디엄급문제.
-> top-down recursive DP + memoization 으로 해봤으나 시간초과..;;
   솔루션 보니까 내가 분명 했던 생각인것같은데, 내가 생각하다가 스쳐지나가버린듯;;;
   해설 되게 좋음. DP의 일반론 얘기함. 백트랙킹, 탑다운 재귀 DP, 바텀업 iterative DP, 등에 대해 얘기.
"""
class Solution:
    def __init__(self):
        self.memo = {}
    def canJump(self, nums: List[int]) -> bool:
        
        def helper(i, nums):     
        
            if nums[i]>=len(nums)-(i+1):
                return True            

            if i in self.memo:
                return self.memo[i]

            can=1 # 1:cant 0:can
            for j in range(i+1, i+nums[i]+1):
                if helper(j, nums):
                    can*=0
                    break
                else:
                    can*=1
            if can==1:
                self.memo[i]=False
                return False
            else:
                self.memo[i]=True
                return True
            
        return helper(0, nums)