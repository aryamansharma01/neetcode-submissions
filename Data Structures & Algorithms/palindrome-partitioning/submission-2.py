class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def helper(i, arr):
            if i==len(s):
                res.append(arr[:])
            for j in range(i,len(s)):
                if s[i:j+1]==s[i:j+1][::-1]:
                    helper(j+1,arr+[s[i:j+1]])
        helper(0,[])
        return res
