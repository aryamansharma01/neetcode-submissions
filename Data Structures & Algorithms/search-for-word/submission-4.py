class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, row, col, used):
            if row>=len(board) or row<0 or col>=len(board[0]) or col<0:
                return False
            if used[row][col]==1 or board[row][col]!=word[i]:
                return False
            if i==len(word)-1:
                return True
            if board[row][col]==word[i] and used[row][col]==0:
                used[row][col] = 1
                a = helper(i+1,row+1,col,used)
                b = helper(i+1,row,col+1,used)
                c = helper(i+1,row-1,col,used)
                d = helper(i+1,row,col-1,used)
                if a or b or c or d:
                    return True
            used[row][col] = 0
            return False
        used = [[0 for i in range(len(board[0]))] for i in range(len(board))]
        val = False

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = val or helper(0,i,j,used)
        return val
        