class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i,arr):
            if i==len(nums):
                if sum(arr)==target:
                    res.append(arr)
                return
            if sum(arr)+nums[i]<=target:
                helper(i,arr+[nums[i]])
            helper(i+1,arr)
            return 
        helper(0,[])
        return res
