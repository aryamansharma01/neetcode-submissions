class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s)<len(t) or (len(s)==len(t) and s!=t):
            return 0
        dp = [[-1 for i in range(len(t))] for j in range(len(s))]
        def helper(i,j):
            if i==0:
                if j>0:
                    return 0
                if s[i]==t[j]:
                    return 1
                return 0
            if j==0:
                cnt = 0
                while i>=0:
                    if s[i]==t[j]:
                        cnt+=1
                    i-=1
                dp[i][j]=cnt
                return cnt
            if dp[i][j]!=-1:
                return dp[i][j]
            take = 0
            if s[i]==t[j]:
                take= helper(i-1,j-1)
            nottake = helper(i-1,j)
            dp[i][j]=take+nottake
            return take+nottake

        return helper(len(s)-1,len(t)-1)
            