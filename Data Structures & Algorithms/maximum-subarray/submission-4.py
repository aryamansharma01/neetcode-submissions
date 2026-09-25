class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(2)]
        
        dp[1] = max(0, nums[0])
        dp[0] = nums[0]
        for i in range(1,n):
            curr = [-1,-1]
            curr[1] = max(0,nums[i]+dp[1])
            curr[0] = max(nums[i]+dp[1],dp[0])
            dp = curr
        return dp[0]
        