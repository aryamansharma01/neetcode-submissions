class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        res = []
        for i, s in enumerate(strs):
            x = "".join(sorted(s))
            if x not in dict:
                dict[x] = [i]
            else:
                dict[x].append(i)
        for i in dict:
            temp = []
            for j in dict[i]:
                temp.append(strs[j])
            res.append(temp)
        return res
            
