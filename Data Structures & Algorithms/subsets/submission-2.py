class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        n = len(nums)
        def helper(i, arr):
            if i==n:
                res.append(arr[:])
                return
            arr.append(nums[i])
            take = helper(i+1,arr)
            arr.pop()
            nottake = helper(i+1,arr)
            return
        helper(0,[])
        return res