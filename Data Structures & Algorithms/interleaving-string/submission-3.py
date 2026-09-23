class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1= len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1+n2!=n3:
            return False
        dp = [[-1 for i in range(n2+1)] for i in range(n1+1)]
        def helper(i,j):
            k = i+j
            if i==0 and j==0:
                return True
            ans = False
            if dp[i][j]!=-1:
                return dp[i][j]
            if i>0 and s1[i-1]==s3[k-1]:
                ans = ans or helper(i-1,j)
            if j>0 and s2[j-1] ==s3[k-1]:
                ans = ans or helper(i,j-1)
            dp[i][j] = ans
            return ans
        
        return helper(n1,n2)