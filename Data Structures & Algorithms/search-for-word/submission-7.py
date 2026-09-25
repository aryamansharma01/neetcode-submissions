class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #m*n matrix
        m = len(board)
        n = len(board[0])

        def helper(i,j,ptr,vis):
            if ptr==len(word):
                return True
            if i>=m or j>=n or i<0 or j<0 or board[i][j]!=word[ptr] or (i,j) in vis:
                return False
            vis.add((i,j))
            for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                if helper(i+dx,j+dy,ptr+1,vis):
                    return True
            vis.remove((i,j))
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if helper(i,j,0,set())==True:
                        return True
        return False

