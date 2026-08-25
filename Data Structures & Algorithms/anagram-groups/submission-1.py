class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        res = []
        for i in strs:
            x = "".join(sorted(i))
            if x not in m:
                m[x] = [i]
            else:
                m[x].append(i)

        for i in m:
            t = []
            for j in m[i]:
                t.append(j)
            res.append(t)
        return res
