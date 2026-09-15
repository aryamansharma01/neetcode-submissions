class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minheap = [-i for i in stones]
        heapq.heapify(minheap)
        while len(minheap)>1:
            x = heapq.heappop(minheap)
            y = heapq.heappop(minheap)
            if x!=y:
                heapq.heappush(minheap,x-y)
        if len(minheap)==1:
            return -heapq.heappop(minheap)
        return 0



            