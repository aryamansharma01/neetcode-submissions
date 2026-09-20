class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1]*n
        def helper(i):
            if i==n-1:
                return True
            if i>=n:
                return False
            res = False
            if dp[i]!=-1:
                return dp[i]
            if nums[i]>0:
                for d in range(1,nums[i]+1):
                    res = res | helper(i+d)
            dp[i] = res
            return res
        return helper(0)