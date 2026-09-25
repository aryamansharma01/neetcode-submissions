class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i,arr):
            if i==len(nums):
                res.append(arr)
                return
            helper(i+1,arr+[nums[i]])
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1
            helper(i+1,arr)
            return
        nums.sort()
        helper(0,[])
        return res