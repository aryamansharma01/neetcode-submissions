class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(n+1):
            adj[i] = []
        for i in times:
            adj[i[0]].append((i[1],i[2]))
        dist = [math.inf]*(n+1)
        q = []
        heapq.heapify(q)
        heapq.heappush(q,(0,k))
        dist[k] = 0
        while q:
            d,ele = heapq.heappop(q)
            for i in adj[ele]:
                if dist[i[0]]>d+i[1]:
                    dist[i[0]] = d+i[1]
                    heapq.heappush(q,(dist[i[0]],i[0]))
        for i in dist[1:]:
            if i==math.inf:
                return -1
        return max(dist[1:])
