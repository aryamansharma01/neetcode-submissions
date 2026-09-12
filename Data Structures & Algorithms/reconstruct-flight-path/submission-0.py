class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        for i in tickets:
            if i[0] not in adj:
                adj[i[0]] = []
            heapq.heappush(adj[i[0]],i[1])
        res = []
        def dfs(i):
            if i in adj:
                while adj[i]:
                    dfs(heapq.heappop(adj[i]))
            res.append(i)
            return 
        dfs("JFK")
        return res[::-1]