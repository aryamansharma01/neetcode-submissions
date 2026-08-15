class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)] for j in range(n)]
        def isvalid(i,j):
            if i<n and j<m and i>=0 and j>=0:
                return True
            return False
        def dfs(i,j):
            vis[i][j] = 1
            if i+1<n and grid[i+1][j]=='1' and vis[i+1][j]==0:
                dfs(i+1,j)
            if i-1>=0 and grid[i-1][j]=='1' and vis[i-1][j]==0:
                dfs(i-1,j)
            if j+1<m and grid[i][j+1]=='1' and vis[i][j+1]==0:
                dfs(i,j+1)
            if j-1>=0 and grid[i][j-1]=='1' and vis[i][j-1]==0:
                dfs(i,j-1)
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and vis[i][j]==0:
                    res+=1
                    dfs(i,j)

        return res


                        