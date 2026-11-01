class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea=0
        n = len(grid)
        m = len(grid[0])
        vis = set()
        def dfs(i,j):
            if grid[i][j]==0:
                return 0
            grid[i][j] = 0
            area = 1
            for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if 0<=x<n and 0<=y<m and grid[x][y]==1:
                    area+=dfs(x,y)
            return area
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    maxarea = max(maxarea, dfs(i,j))
        return maxarea
                    


