class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for i in range(m)] for j in range(n)]
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append(((i,j),0))
                    vis[i][j] = 2
        res = 0
        while q:
            ((i,j), t) = q.popleft()
            if i+1<n:
                if grid[i+1][j]==1 and vis[i+1][j]!=2:
                    vis[i+1][j] = 2
                    q.append(((i+1,j),t+1))
                    res = max(res, t+1)
            if i-1>=0:
                if grid[i-1][j]==1 and vis[i-1][j]!=2:
                    vis[i-1][j] = 2
                    q.append(((i-1,j),t+1))
                    res = max(res, t+1)
            if j+1<m:
                if grid[i][j+1]==1 and vis[i][j+1]!=2:
                    vis[i][j+1] = 2
                    q.append(((i,j+1),t+1))
                    res = max(res, t+1)
            if j-1>=0:
                if grid[i][j-1]==1 and vis[i][j-1]!=2:
                    vis[i][j-1] = 2
                    q.append(((i,j-1),t+1))
                    res = max(res, t+1)
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and vis[i][j]==0:
                    return -1
        return res

                