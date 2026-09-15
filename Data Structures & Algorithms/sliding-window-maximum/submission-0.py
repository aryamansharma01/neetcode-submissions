class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        n = len(nums)
        for i in range(k):
            while q and q[-1][0]<nums[i]:
                q.pop()
            q.append((nums[i],i)) 
        res.append(q[0][0])
        for i in range(k,n):
            while q and q[-1][0]<nums[i]:
                q.pop()
            q.append((nums[i],i)) 
            if q[0][1]<=i-k:
                q.popleft()
            res.append(q[0][0])
        return res
