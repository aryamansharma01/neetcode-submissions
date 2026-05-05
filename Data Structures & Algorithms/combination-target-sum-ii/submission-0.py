class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(arr, ind, target, res):
            if target==0:
                res.append(arr[:])
                return
            for i in range(ind, len(candidates)):
                if candidates[i]==candidates[i-1] and i>ind:
                    continue
                if candidates[i]>target:
                    break
                arr.append(candidates[i])
                helper(arr,i+1,target-candidates[i],res)
                arr.pop()
        candidates.sort()
        res = []
        helper([],0,target,res)
        return res