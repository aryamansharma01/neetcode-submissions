class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]
        
        for i in range(1,m):
            curr = [1 for i in range(n)]
            curr[0] = 1
            for j in range(1,n):
                curr[j] = dp[j] + curr[j-1]
            dp = curr
        return dp[n-1]
        