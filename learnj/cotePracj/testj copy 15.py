class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        
        # self.memo = [[None]*(target+1) for _ in range(d+1)]    # use: memo[d][target]      
        self.memo = {}  
        ret = self.numtotar(d,f,target)
        return ret % (10**9+7)
    
    def numtotar(self, d,f,target):

        
        if (d,target) in self.memo:
            return self.memo[(d,target)]

        if target<=0:
            return 0         
        
        if d==1:
            if f >= target:
                return 1
            else:
                return 0                   

        
        self.memo[(d,target)] = sum([self.numtotar(d-1,f,target-i) for i in range(1,f+1)])
        return self.memo[(d,target)]
        # return sum([self.numtotar(d-1,f,target-i) for i in range(1,f+1)])

solution = Solution()
d,f,target = 30,30,500
ret=solution.numRollsToTarget(d,f,target)
print('ret:',ret)
# print('memo:',solution.memo)