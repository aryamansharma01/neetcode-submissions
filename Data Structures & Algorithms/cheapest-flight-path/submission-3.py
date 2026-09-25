class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist  = [math.inf]*n
        adj = {i:[] for i in range(n)}
        for i in flights:
            adj[i[0]].append((i[1],i[2]))
        dist[src] = 0
        q = deque()
        q.append((0,0,src))
        while  q:
            stops, d, ele = q.popleft()
            if stops>k:
                continue
            for i in adj[ele]:
                if dist[i[0]]>d+i[1] and stops<=k:
                    dist[i[0]] = d+i[1]
                    q.append((stops+1,d+i[1],i[0]))
        if dist[dst]==math.inf:
            return -1
        return dist[dst]





