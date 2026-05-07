import math 
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(amount):
            if amount==0:
                return 0
            if dp[amount]!=-1:
                return dp[amount] 
            res = math.inf
            #pick case
            for coin in coins:
                if amount>=coin:
                    res = min(res, 1+helper(amount-coin))
            dp[amount] = res
            return res
        
        dp = [-1]*(amount+1)
        dp[0] = 0
        res = helper(amount)
        if res==math.inf:
            return -1
        return res
            