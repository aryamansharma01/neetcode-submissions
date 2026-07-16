class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for i in range(amount+1)] for i in range(n)]
        def helper(i, s):
            if s==0:
                dp[i][s] = 1
                return 1
            if i==0:
                if s%coins[i]==0:
                    dp[i][s]=1
                    return 1
                else:
                    dp[i][s] =0 
                return 0
            if dp[i][s]!=-1:
                return dp[i][s]
            take = 0
            if s>=coins[i]:
                take = helper(i,s-coins[i])
            nottake = helper(i-1,s)
            dp[i][s] = take+nottake
            return take+nottake
        return helper(n-1,amount)

        