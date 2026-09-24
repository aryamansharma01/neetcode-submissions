class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i,arr):
            if i==len(nums):
                res.append(arr)
                return
            helper(i+1,arr+[nums[i]])
            helper(i+1,arr)
            return
        helper(0,[])
        return res