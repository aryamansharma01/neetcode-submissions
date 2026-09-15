class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = []
        vis = set()
        heapq.heappush(q,(0,points[0][0],points[0][1]))
        s = 0
        while q :
            d, x, y = heapq.heappop(q)
            if (x,y) in vis:
                continue
            vis.add((x,y))
            s+=d
            for i in points:
                if i!=[x,y]:
                    d=abs(i[0]-x)+abs(i[1]-y)
                    minx = i[0]
                    miny = i[1]
                    heapq.heappush(q,(d,minx,miny))
        return s


