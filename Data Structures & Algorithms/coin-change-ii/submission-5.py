class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[i]=1
        for i in range(1,n):
            curr = [0 for i in range(amount+1)]
            curr[0] = 1
            for j in range(1,amount+1):
                take = 0
                if j>=coins[i]:
                    take = curr[j-coins[i]]
                nottake = dp[j]
                curr[j] = take+nottake
            dp = curr
        return dp[amount]

        