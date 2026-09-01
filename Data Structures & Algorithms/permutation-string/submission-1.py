class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        def check(s1,s2):
            if sorted(s1)==sorted(s2):
                return True
            return False
        n1 = len(s1)
        n2 = len(s2)
        l,r = 0,n1-1
        for i in range(n2-r):
            if check(s1,s2[i:i+r+1]):
                return True
        return False




            

        