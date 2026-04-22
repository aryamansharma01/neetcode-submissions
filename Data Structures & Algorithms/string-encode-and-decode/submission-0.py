class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+=f"{len(i)}*"
            s+=i
        print(s)
        return s

    def findlength(self, s: str):
        i,j = 0,0
        while j<len(s) and s[j]!='*':
            j+=1
        n = s[i:j]
        print(n)
        return n

    def decode(self, s: str) -> List[str]:
        res = []
        i,j = 0,0
        while i < len(s) and j < len(s):
            n = self.findlength(s[i:])
            while s[i]!="*":
                i+=1
            j = i+int(n)
            res.append(s[i+1:j+1])
            s = s[j+1:]
            i,j = 0,0
        return res
            

