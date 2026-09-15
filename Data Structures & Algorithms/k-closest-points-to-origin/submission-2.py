class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for i in points:
            dist.append(((i[0]**2+i[1]**2)**0.5,i))
        heapq.heapify(dist)
        res = []
        for i in range(k):
            d, i = heapq.heappop(dist)
            res.append(i)
        return res