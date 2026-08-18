class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        vis = [0]*n
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        def dfs(i):
            vis[i]=1
            for j in adj[i]:
                if vis[j]!=1:
                    dfs(j)
        path = 0
        for i in range(n):
            if vis[i]==0:
                dfs(i)
                path+=1
        return path