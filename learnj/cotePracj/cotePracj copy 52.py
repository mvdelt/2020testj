"""
LeetCode 'Coin change' 미디엄급문제. 보니까 이미 예전에 풀엇엇네. 그래도 다시풀어봄.
"""
from typing import List
class Solution:
    def __init__(self):
        self.memo={}
    def coinChange(self, coins: List[int], amount: int) -> int:
        ret = self.helper(coins, amount)
        if ret == float('inf'):
            return -1
        else:
            return ret

    def helper(self, coins, sumj):
        if sumj == 0:
            return 0

        elif sumj < 0:
            return float('inf')

        if sumj in self.memo:
            return self.memo[sumj]
        else:
            self.memo[sumj] = min(self.helper(coins, sumj-coinval) for coinval in coins) + 1
            return self.memo[sumj]


            
            
