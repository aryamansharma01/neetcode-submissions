class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def helper(i,s,arr):
            if s==target:
                res.append(arr)
            if i==len(candidates):
                return
            for j in range(i, len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if candidates[j]>target:
                    break
                if s+candidates[j]<=target:
                    helper(j+1,s+candidates[j],arr+[candidates[j]])
        helper(0,0,[])
        return res