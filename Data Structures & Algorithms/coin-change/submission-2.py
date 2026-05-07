import math 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1]*(amount+1)
        dp[0] = 0
        if amount==0:
            return 0
        for i in range(1, amount+1):
            res = math.inf
            for coin in coins:
                if i>=coin:
                    res = min(res, 1+dp[i-coin])
            dp[i] = res
        if dp[amount]==math.inf:
            return -1
        return dp[amount]
            