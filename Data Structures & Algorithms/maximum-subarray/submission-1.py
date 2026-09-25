class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1 for i in range(2)] for j in range(n)]
        def helper(i,flag):
            if i==0:
                if flag==True:
                    return max(0,nums[i])
                return nums[i]
            if dp[i][flag]!=-1:
                return dp[i][flag]
            if flag==False:
                take = nums[i]+helper(i-1, True)
                nottake = helper(i-1,False)
                dp[i][flag] = max(take,nottake)
                return max(take,nottake)
            take = nums[i]+helper(i-1,True)
            nottake = 0
            dp[i][flag] = max(take,nottake)
            return max(take,nottake)
        return helper(n-1,0)
        