class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1 for i in range(n2+1)] for i in range(n1+1)]
        # def helper(i,j):
        #     if i<0 or j<0:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     if text1[i]==text2[j]:
        #         dp[i][j] = 1+helper(i-1,j-1)
        #         return dp[i][j]
        #     dp[i][j] = max(helper(i-1,j),helper(i,j-1))
        #     return dp[i][j]
        
        # for i in range(n1):
        #     for j in range(n2):
        #         if i==0 or j==0:
        #             if text1[i]==text2[j]:
        #                 dp[i][j]=1
                    
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                    continue
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[n1][n2]
        