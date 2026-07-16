class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for i in range(amount+1)] for i in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
            else:
                dp[0][i] =0 
        for i in range(1,n):
            for j in range(1,amount+1):
                take = 0
                if j>=coins[i]:
                    take = dp[i][j-coins[i]]
                nottake = dp[i-1][j]
                dp[i][j] = take+nottake
        return dp[n-1][amount]

        