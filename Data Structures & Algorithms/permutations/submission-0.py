class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(arr, ptr, res):
            if ptr==len(arr):
                res.append(arr[:])
                return
            for i in range(ptr, len(arr)):
                arr[i],arr[ptr] = arr[ptr],arr[i]
                helper(arr,ptr+1,res)
                arr[i],arr[ptr] = arr[ptr],arr[i]
        res = []
        helper(nums, 0, res)
        return res
        