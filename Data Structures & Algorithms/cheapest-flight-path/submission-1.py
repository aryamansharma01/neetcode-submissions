class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in flights:
            adj[i[0]].append((i[1],i[2]))
        q = []
        dist = [math.inf]*n
        heapq.heapify(q)
        heapq.heappush(q,(0,src,0))
        dist[src] = 0
        while q:
            stops, ele, d = heapq.heappop(q)
            if stops>k:
                continue
            for i in adj[ele]:
                if dist[i[0]]>d+i[1] and stops<=k:
                    dist[i[0]]= d+i[1]
                    heapq.heappush(q,(stops+1,i[0],dist[i[0]]))
        if dist[dst]==math.inf:
            return -1
        return dist[dst]
