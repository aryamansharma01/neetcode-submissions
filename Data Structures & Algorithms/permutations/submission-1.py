class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i,arr):
            if i==len(nums):
                res.append(arr[:])
            #no reverse
            for j in range(i,len(nums)):
                arr[j],arr[i] = arr[i],arr[j]
                helper(i+1,arr)
                arr[j],arr[i] = arr[i],arr[j]
        helper(0,nums)
        return res