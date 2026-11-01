class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(opens,closes,s):
            if opens==n and closes==n:
                res.append(s)
                return
            if opens<n:
                helper(opens+1,closes,s+"(")
            if closes<opens:
                helper(opens,closes+1,s+")")
        helper(0,0,"")
        return res
