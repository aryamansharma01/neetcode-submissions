class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        directlyconnected = set()
        def dfs(i,j):
            directlyconnected.add((i,j))
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<n and 0<=y<m and board[x][y]=='O' and (x,y) not in directlyconnected:
                    dfs(x,y)
        for i in range(n):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][m-1]=='O':
                dfs(i,m-1)
        for j in range(m):
            if board[0][j]=='O':
                dfs(0,j)
            if board[n-1][j]=='O':
                dfs(n-1,j)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O' and (i,j) not in directlyconnected:
                    board[i][j]='X'
        return

