class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for i in range(n2)] for j in range(n1)]
        def helper(i,j):
            if i<0 or j<0:
                return 0
            take = -math.inf
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i]==text2[j]:
                take = 1+helper(i-1,j-1)
            nottake = max(helper(i-1,j),helper(i,j-1))
            dp[i][j] = max(take,nottake)
            return max(take,nottake)
        return helper(n1-1,n2-1)