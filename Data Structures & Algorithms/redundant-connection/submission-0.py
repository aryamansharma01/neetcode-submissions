class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        root = [i for i in range(len(edges)+1)]
        size = [1]*(len(edges)+1)
        root[0] = -1
        size[0] = -1
        def findroot(u):
            if root[u] ==u:
                return u
            return root[root[u]]
        res = []
        for i in edges:
            u,v = i[0],i[1]
            ru = findroot(u)
            rv = findroot(v)
            if ru==rv:
                res = [u,v]
            elif size[ru]<size[rv]:
                root[ru] = rv
                size[rv]+=size[ru]
            else:
                root[rv] = ru
                size[ru]+=size[rv]
        return res
                