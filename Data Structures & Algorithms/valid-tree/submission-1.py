class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        if len(edges)!=n-1:
            return False
        for i in edges:
            u = i[0]
            v = i[1]
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)
        vis = set()
        def cycle(i,parent):
            vis.add(i)
            for j in adj.get(i,[]):
                if j==parent:
                    continue
                if j in vis:
                    return True
                if cycle(j,i):
                    return True
            return False
        return not cycle(0,-1) and len(vis)==n


