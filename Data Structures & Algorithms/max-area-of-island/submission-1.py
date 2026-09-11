class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea=0
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        def dfs(i,j):
            area = 1
            vis[i][j]=1
            if i+1<n and vis[i+1][j]==0 and grid[i+1][j]==1:
                area+=dfs(i+1,j)
            if j+1<m and vis[i][j+1]==0 and grid[i][j+1]==1:
                area+=dfs(i,j+1)
            if i-1>=0 and vis[i-1][j]==0 and grid[i-1][j]==1:
                area+=dfs(i-1,j)
            if j-1>=0 and vis[i][j-1]==0 and grid[i][j-1]==1:
                area+=dfs(i,j-1)
            return area
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    if vis[i][j]==0:
                        maxarea = max(maxarea,dfs(i,j))
                    else:
                        continue
        return maxarea

