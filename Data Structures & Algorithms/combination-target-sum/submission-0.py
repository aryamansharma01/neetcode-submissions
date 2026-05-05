class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(arr, ind, target, res):
            if target==0:
                res.append(arr[:])
                return
            for i in range(ind, len(nums)):
                if nums[i]<=target:
                    arr.append(nums[i])
                    helper(arr,i,target-nums[i],res)
                    arr.pop()

        res = []
        helper([],0,target,res)
        return res
        