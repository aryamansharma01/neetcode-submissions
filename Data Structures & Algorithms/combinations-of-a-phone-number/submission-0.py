class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digimap = {'2':['a','b','c'], '3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        def helper(path, i, res):
            if i == len(digits):
                res.append(path[:])
                return
            digit = digits[i]
            for j in digimap[digit]:
                path+=j
                helper(path,i+1,res)
                path=path[:-1]
        res = []
        if digits=='':
            return []
        helper('',0,res)
        return res
        