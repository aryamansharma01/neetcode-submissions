class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def helper(i, s):
            if i==0:
                sub = (s-nums[i]==target)
                add = (s+nums[i]==target)
                return sub+add
            add_curr = helper(i-1,s+nums[i])
            sub_curr = helper(i-1,s-nums[i])
            return add_curr + sub_curr
        return helper(n-1,0)
            
        