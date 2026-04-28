class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k):
            return sum([i//k if i%k ==0 else 1+(i//k) for i in piles])
        l = 1
        r = max(piles)

        while l<r:
            mid = (l+r)//2
            if helper(mid)>h:
                l = mid+1
            else:
                r = mid
        return l

        