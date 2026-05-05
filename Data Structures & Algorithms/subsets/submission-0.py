class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(arr, i, res):
            if i==len(nums):
                res.append(arr[:])
                return
            arr.append(nums[i])
            helper(arr,i+1,res)
            arr.pop()
            helper(arr,i+1,res)
        res = []
        helper([],0,res)
        return res
        