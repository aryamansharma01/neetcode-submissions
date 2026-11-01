class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        def helper(i,j,vis,ptr):
            if ptr==len(word):
                return True
            if i<0 or i>=r or j<0 or j>=c or (i,j) in vis or board[i][j]!=word[ptr]:
                return False
            vis.add((i,j))
            for x,y in [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]:
                if helper(x,y,vis,ptr+1):
                    return True
            vis.remove((i,j))
            return False
        res = False
        for i in range(r):
            for j in range(c):
                res = helper(i,j,set(),0)
                if res:
                    return True
        return res
        