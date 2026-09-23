class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for i in range(n)]
        def helper(i):
            if i==n-1:
                return 0
            if i>=n:
                return math.inf
            if dp[i]!=-1:
                return dp[i]
            res = math.inf
            for d in range(1,nums[i]+1):
                res = min(res,1+helper(i+d))
            dp[i] = res
            return res
        return helper(0)