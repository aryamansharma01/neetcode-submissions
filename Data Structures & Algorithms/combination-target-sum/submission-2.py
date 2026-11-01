class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i,s,arr):
            if s==target:
                res.append(arr[:])
                return
            if i==len(nums):
                return
            if s+nums[i]<=target:
                helper(i,s+nums[i],arr+[nums[i]])
            helper(i+1,s,arr)
        helper(0,0,[])
        return res