class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2!=0:
            return False
        s= int(s/2)
        n = len(nums)
        dp = [[False for i in range(s+1)] for i in range(n)]
        # def helper(i, s):
        #     if i==0:
        #         dp[i] = (nums[i]==s)
        #         return nums[i]==s
        #     if dp[i][s]!=-1:
        #         return dp[i][s]
        #     nottake = helper(i-1,s)
        #     take = False
        #     if s-nums[i]>=0:
        #         take = helper(i-1,s-nums[i])
        #     dp[i][s] = (nottake or take)
        #     return nottake or take
        dp[0][0] = True
        for i in range(s+1):
            dp[0][i] = (nums[0]==i)
        for i in range(1,n):
            for j in range(s+1):
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[n-1][s]
            
        