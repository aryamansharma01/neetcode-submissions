class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set()
        for i in wordDict:
            wordset.add(i)
        n = len(s)
        dp = [-1]*len(s)
        def helper(i):
            if i==n:
                return True
            if dp[i]!=-1:
                return dp[i]
            for j in range(i,n+1):
                if s[i:j] in wordset and helper(j):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        return helper(0)

