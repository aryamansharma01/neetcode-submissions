class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxval = min(len(i) for i in strs)
        for r in range(maxval):
            c = strs[0][r]
            for i in strs:
                if i[r]!=c:
                    return i[:r]
        return strs[0][:maxval]
