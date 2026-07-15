class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s%2!=0:
            return False
        s= int(s/2)
        n = len(nums)
        dp = [False for i in range(s+1)]
        dp[0] = True
        for i in range(s+1):
            dp[i] = (nums[0]==i)
        for i in range(1,n):
            curr = [False] * (s + 1)
            curr[0] = True
            for j in range(s+1):
                curr[j] = dp[j] or dp[j-nums[i]]
            dp = curr
        return dp[s]
            
        