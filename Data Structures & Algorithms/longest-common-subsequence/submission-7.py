class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                take = -math.inf
                if text1[i]==text2[j]:
                    take = 1+dp[i-1][j-1]
                nottake = max(dp[i-1][j],dp[i][j-1])
                dp[i][j] = max(take,nottake)
        return dp[n1-1][n2-1]