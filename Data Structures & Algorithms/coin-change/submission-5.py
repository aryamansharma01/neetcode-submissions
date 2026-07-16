import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        def helper(i,amount):
            if amount==0:
                return 0
            if i==0:
                if amount>=coins[i]:
                    if amount%coins[i]==0:
                        return amount//coins[i]
                return math.inf
            take = math.inf
            if amount>=coins[i]:
                take = 1+helper(i,amount-coins[i])
            nottake = helper(i-1,amount)
            return min(take,nottake)
        ans = helper(n-1,amount)
        if ans ==math.inf :
            return -1
        return ans

