class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {0:1}
        n = len(nums)
        cursum=0
        cnt = 0
        for i in nums:
            cursum+=i
            cnt+=m.get(cursum-k,0)
            m[cursum] = m.get(cursum,0)+1
        return cnt
            



