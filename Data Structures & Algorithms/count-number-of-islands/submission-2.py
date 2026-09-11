class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        vis = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        def dfs(i,j):
            vis[i][j] = 1
            if i+1<len(grid) and grid[i+1][j]=="1" and vis[i+1][j]==0:
                dfs(i+1,j)
            if j+1<len(grid[0]) and grid[i][j+1]=="1" and vis[i][j+1]==0:
                dfs(i,j+1)
            if i-1>=0 and grid[i-1][j]=="1" and vis[i-1][j]==0:
                dfs(i-1,j)
            if j-1>=0 and grid[i][j-1]=="1" and vis[i][j-1]==0:
                dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    if vis[i][j]==0:
                        cnt+=1
                        dfs(i,j)
                    else:
                        continue
        return cnt
                
            