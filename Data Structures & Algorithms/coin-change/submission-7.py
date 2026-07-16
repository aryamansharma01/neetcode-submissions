import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n= len(coins)
        # def helper(i,amount):
        #     if amount==0:
        #         return 0
            # if i==0:
            #     if amount>=coins[i]:
            #         if amount%coins[i]==0:
            #             return amount//coins[i]
            #     return math.inf
            # take = math.inf
            # if amount>=coins[i]:
            #     take = 1+helper(i,amount-coins[i])
            # nottake = helper(i-1,amount)
            # return min(take,nottake)
        dp = [-1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            if i%coins[0]==0:
                dp[i] = i//coins[0]
            else:
                dp[i] = math.inf
        for i in range(1,n):
            curr = [-1 for i in range(amount+1)]
            curr[0] = 0
            for j in range(amount+1):
                if coins[i] <= j:
                    curr[j] = min(1+curr[j-coins[i]],dp[j])
                else:
                    curr[j] = dp[j]
            dp = curr
        ans = dp[amount]
        if ans ==math.inf :
            return -1
        return ans

