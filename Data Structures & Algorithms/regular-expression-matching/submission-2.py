class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[-1 for i in range(len(s))] for j in range(len(p))]
        def helper(i,j):
            if i==len(p):
                if j==len(s):
                    return True
                return False
            if j==len(s):
                while i<len(p):
                    if i + 1 >= len(p) or p[i + 1] != '*':
                        return False
                    i += 2
                return True
            if dp[i][j]!=-1:
                return dp[i][j]
            if i+1<len(p) and p[i+1]=='*':
                res = helper(i+2,j)
                if p[i]==s[j] or p[i]=='.':
                    res = res or helper(i,j+1)
                dp[i][j] = res
                return dp[i][j]
            if p[i]=='.':
                dp[i][j] = helper(i+1,j+1)
                return dp[i][j]
            if p[i]==s[j]:
                dp[i][j] = helper(i+1,j+1)
                return dp[i][j]
            dp[i][j] = False
            return False
        return helper(0,0)