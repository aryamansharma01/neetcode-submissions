class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1 for i in range(2)] for i in range(n)]
        def helper(i,canbuy):
            if i>=n:
                return 0
            if dp[i][canbuy]!=-1:
                return dp[i][canbuy]
            if canbuy==True:
                profit = max(-prices[i]+helper(i+1,False),helper(i+1,True))
            else:
                profit = max(prices[i]+helper(i+2,True),helper(i+1,False))
            dp[i][canbuy] = profit
            return profit
        return helper(0,True)