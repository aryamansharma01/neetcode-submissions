class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for i in range(n)] for i in range(m)]
        def helper(i,j):
            if i==0 and j==0:
                dp[i][j] = 1
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up = helper(i-1,j)
            right = helper(i,j-1)
            dp[i][j] = up+right
            return up+right
        return helper(m-1,n-1)
        