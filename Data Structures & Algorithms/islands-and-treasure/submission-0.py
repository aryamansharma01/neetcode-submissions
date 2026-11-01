class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31-1
        r = len(grid)
        c = len(grid[0])
        q = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j]==0:
                    q.append((i,j,1))
        while q:
            i,j,d = q.popleft()
            for x,y in [(i+1,j),(i,j+1),(i,j-1),(i-1,j)]:
                if 0<=x<r and 0<=y<c and grid[x][y]!=-1:
                    if grid[x][y]>d:
                        grid[x][y] = d
                        q.append((x,y,d+1))
        return