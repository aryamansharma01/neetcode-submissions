class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r,maxlen,maxf = 0,0,0,0
        m = {}

        while r<len(s):
            if s[r] in m:
                m[s[r]]+=1
            else:
                m[s[r]] = 1
            maxf = max(maxf,m[s[r]])

            if r-l+1 - maxf>k:
                m[s[l]]-=1
                l+=1
            maxlen = max(maxlen, r-l+1)
            r+=1
        return maxlen

        