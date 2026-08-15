class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for i in range(m)] for j in range(n)]
        def isvalid(i,j):
            if i>=0 and j>=0 and i<n and j<m:
                return True
            return False
        def dfs(i,j):
            area = 1
            visited[i][j] = 1
            if isvalid(i+1,j) and grid[i+1][j] ==1 and visited[i+1][j]==0:
                area+=dfs(i+1,j)
            if isvalid(i-1,j) and grid[i-1][j] ==1 and visited[i-1][j]==0:
                area+=dfs(i-1,j)
            if isvalid(i,j+1) and grid[i][j+1] ==1 and visited[i][j+1]==0:
                area+=dfs(i,j+1)
            if isvalid(i,j-1) and grid[i][j-1] ==1 and visited[i][j-1]==0:
                area+=dfs(i,j-1)
            return area
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and visited[i][j]==0:
                    res = max(res, dfs(i,j))
        return res

                
