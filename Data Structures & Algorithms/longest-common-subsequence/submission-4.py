class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [0 for i in range(n2+1)]
        dp[0] = 0
                    
        for i in range(1,n1+1):
            curr = [0 for i in range(n2+1)]
            curr[0] = 0
            for j in range(1,n2+1):
                if text1[i-1]==text2[j-1]:
                    curr[j] = 1+dp[j-1]
                else:
                    curr[j] = max(dp[j],curr[j-1])
            dp = curr

        return dp[n2]
        