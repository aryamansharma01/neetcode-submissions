class Solution:
    def isvalid(self, s):
        return s == s[::-1]
    def partition(self, s: str) -> List[List[str]]:
        def helper(ptr, path, res):
            if ptr==len(s):
                res.append(path[:])
            for i in range(ptr, len(s)):
                if self.isvalid(s[ptr:i+1]):
                    path.append(s[ptr:i+1])
                    helper(i+1,path,res)
                    path.pop()
        res = []
        helper(0,[],res)
        return res
        