class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for i in range(n+1)] for i in range(n+1)]
        # def helper(i,prev):
        #     if i==n:
        #         return 0
        #     take = -1
        #     if dp[i][prev]!=-1:
        #         return dp[i][prev]
        #     if prev==-1 or nums[i]>nums[prev]:
        #         take = 1+ helper(i+1,i)
        #     nottake = helper(i+1,prev)
        #     dp[i][prev]= max(take,nottake)
        #     return max(take,nottake)
        # return helper(0,-1)
        for i in range(n-1,-1,-1):
            for prev in range(i-1,-2,-1):
                take = 0
                if prev ==-1 or nums[i]>nums[prev]:
                    take = 1+ dp[i+1][i+1]
                nottake = dp[i+1][prev+1]
                dp[i][prev+1]= max(take,nottake)
        return dp[0][0]