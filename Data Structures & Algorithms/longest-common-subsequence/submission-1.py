class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for i in range(n2)] for i in range(n1)]
        def helper(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                dp[i][j] = 1+helper(i-1,j-1)
                return dp[i][j]
            dp[i][j] = max(helper(i-1,j),helper(i,j-1))
            return dp[i][j]
        return helper(n1-1,n2-1)
        