class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        ind = [0]*numCourses
        for i in range(numCourses):
            adj[i] = []
        for i in prerequisites:
            ind[i[0]]+=1
            adj[i[1]].append(i[0])
        q = deque()
        res = []
        for i in range(numCourses):
            if ind[i]==0:
                q.append(i)
        if not q:
            return []
        while q:
            ele = q.popleft()
            res.append(ele)
            for i in adj[ele]:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
        if len(res)<numCourses:
            return []
        return res