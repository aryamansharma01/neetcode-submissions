class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # def func(i):
        #     if i <=1:
            #     return 0
            
            # if dp[i]!=-1:
            #     return dp[i]
            # prev = func(i-1) + cost[i-1]
            # prev2 = func(i-2)+cost[i-2]
            # return dp[i] = min(prev,prev2)

        dp = [-1]*(len(cost)+1)
        prev1 = prev2 = 0
        for i in range(2,len(cost)+1):
            curr = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev2 = prev1
            prev1 = curr
            
        return prev1
            
            
        