class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        q = deque()
        vis = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    vis.add((i,j))

        while q:
            i,j,t = q.popleft()
            for x,y in [(i+1,j),(i-1,j),(i,j-1),(i,j+1)]:
                if 0<=x<n and 0<=y<m and grid[x][y]==1 and (x,y) not in vis:
                    vis.add((x,y))
                    q.append((x,y,t+1))
                    grid[x][y] = 2
                    res = max(res,t+1)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return res

