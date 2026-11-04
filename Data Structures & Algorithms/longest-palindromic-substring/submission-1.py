class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [0]*(n+1)
        maxval = 0
        rev = s[::-1]
        end_idx = -1 
        for i in range(1,n+1):
            curr = [0]*(n+1)
            for j in range(1,n+1):
                if s[i-1]==rev[j-1]:
                    curr[j] = 1+dp[j-1]
                    start_s = i - curr[j]
                    start_rev = n - j

                    if start_s == start_rev and curr[j] > maxval:
                        maxval = curr[j]
                        end_idx = i
            dp = curr
        return s[end_idx-maxval:end_idx]