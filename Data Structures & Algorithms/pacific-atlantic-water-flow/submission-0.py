class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        r = len(heights)
        c = len(heights[0])

        def dfs(i,j, ocean):
            ocean.add((i,j))
            for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if 0<=x<r and 0<=y<c and heights[x][y]>=heights[i][j] and (x,y) not in ocean:
                    dfs(x,y,ocean)
            return

        for i in range(r):
            dfs(i, 0, pacific)
            dfs(i,c-1,atlantic)
        for j in range(c):
            dfs(0,j,pacific)
            dfs(r-1,j,atlantic)

        return [[x,y] for x,y in (pacific & atlantic)]