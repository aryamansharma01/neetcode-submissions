class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r, maxlen = 0,0,0
        m = {}
        while (r<len(s)):
            if (s[r] in m):
                if m[s[r]]>=l:
                    l = m[s[r]]+1
            maxlen = max(maxlen,r-l+1)
            m[s[r]]=r
            r+=1
        return maxlen