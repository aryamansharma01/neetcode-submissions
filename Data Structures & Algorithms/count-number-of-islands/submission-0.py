class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)] for j in range(n)]
        def isvalid(i,j):
            if i<n and j<m and i>=0 and j>=0:
                return True
            return False
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1' and vis[i][j]==0:
                    res+=1
                    q = deque()
                    q.append((i,j))
                    vis[i][j] = 1
                    while q:
                        r, c = q.popleft()
                        for di in range(-1,2):
                            for dj in range(-1,2):
                                if isvalid(r+di,c) and grid[r+di][c]=='1' and vis[r+di][c]==0:
                                    vis[r+di][c]=1
                                    q.append((r+di,c))
                                if isvalid(r,c+dj) and grid[r][c+dj]=='1' and vis[r][c+dj]==0:
                                    vis[r][c+dj]=1
                                    q.append((r,c+dj))
        return res


                        