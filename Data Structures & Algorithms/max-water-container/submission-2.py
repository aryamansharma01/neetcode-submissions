class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        res = 0
        while l<r:
            res = max(res,min(heights[l],heights[r])*(r-l))
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return res
            

