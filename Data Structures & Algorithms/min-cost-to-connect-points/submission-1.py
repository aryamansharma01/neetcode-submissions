class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        q = []
        heapq.heappush(q,(0,points[0][0],points[0][1]))
        vis = set()
        cost = 0
        while q:
            d,x,y = heapq.heappop(q)
            if (x,y) in vis:
                continue
            cost+=d
            for i in points:
                if (i[0],i[1]) not in vis:
                    dist = abs(x-i[0])+abs(y-i[1])
                    heapq.heappush(q,(dist,i[0],i[1]))
                    vis.add((x,y))
        return cost
            
