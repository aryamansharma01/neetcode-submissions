class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isvalid(s):
            return s==s[::-1]
        def helper(ptr, arr):
            if ptr==len(s):
                res.append(arr)
            for i in range(ptr,len(s)):
                if isvalid(s[ptr:i+1]):
                    helper(i+1,arr+[s[ptr:i+1]])
        helper(0,[])
        return res