class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        vis = [0]*n
        for i in range(n):
            adj[i] = []
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        def dfs(i, parent):
            vis[i] = 1
            for j in adj[i]:
                if j==parent:
                    continue
                if vis[j]==1:
                    return False
                if dfs(j,i)==False:
                    return False
            return True
        if not dfs(0,-1):
            return False
        for i in vis:
            if i==0:
                return False
        return True