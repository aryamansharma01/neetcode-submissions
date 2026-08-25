class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        q = []
        m = {}
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i] = 1
        for i in m:
            heapq.heappush(q,(m[i],i))
        while len(q)>k:
            heapq.heappop(q)
        res =[]
        while q:
            res.append(heapq.heappop(q)[1])
        return res