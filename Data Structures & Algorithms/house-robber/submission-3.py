#top down  approach -1 
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        #translate recursive to for loop
        #dp[i] = max(nums[i]+dp[i-2], 0 + dp[i-1])
        dp[0] = nums[0]
        if len(nums)==1:
            return dp[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i]+dp[i-2], 0 + dp[i-1])

        return dp[len(nums)-1]
        