class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(nums: List[int]) -> int:
            n = len(nums)
            if n==1:
                return nums[0]
            if n==2:
                return max(nums[0],nums[1])
            prev = max(nums[1],nums[0])
            prev2 = nums[0]
            for i in range(2, len(nums)):
                curr = max(nums[i]+prev2,prev)
                prev2 = prev
                prev = curr
            
            return prev
        if  len(nums)==1:
            return nums[0]
        return max(solve(nums[:-1]),solve(nums[1:]))