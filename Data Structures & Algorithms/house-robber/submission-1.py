#bottom up approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        def func(i): #recursive function for max sum until this house
            if i==0:
                dp[i] = nums[i]
                return dp[i]
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            pick = nums[i] + func(i-2)
            npick = 0 + func(i-1)
            dp[i] = max(pick, npick)
            return dp[i]
        dp = [-1]*len(nums)
        return func(len(nums)-1)
        