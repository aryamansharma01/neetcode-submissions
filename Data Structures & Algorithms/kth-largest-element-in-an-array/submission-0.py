class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-i for i in nums]
        heapq.heapify(arr)
        while k>1:
            heapq.heappop(arr)
            k-=1
        return -heapq.heappop(arr)