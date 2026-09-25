class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}
        def helper(ind, currsum):
            if ind==0:
                res = 0
                if currsum+nums[ind]==target:
                    res+=1
                if currsum-nums[ind]==target:
                    res+=1
                dp[(ind,currsum)] = res
                return res
            if (ind,currsum) in dp:
                return dp[(ind,currsum)]
            add = helper(ind-1,currsum+nums[ind])
            sub = helper(ind-1,currsum-nums[ind])
            dp[(ind,currsum)] = add+sub
            return add+sub
        
        n = len(nums)
        return helper(n-1,0)

