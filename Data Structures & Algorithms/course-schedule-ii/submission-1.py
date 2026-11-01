class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0]*numCourses
        adj = {}
        for i in prerequisites:
            u = i[0]
            v = i[1]
            if v not in adj:
                adj[v] = []
            adj[v].append(u)
            ind[u]+=1
        q = deque()
        res = []
        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)
        while q:
            ele =q.popleft()
            res.append(ele)
            for i in adj.get(ele,[]):
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
        if len(res)!=numCourses:
            return []
        return res
