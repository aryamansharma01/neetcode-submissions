class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = defaultdict(int)
        res = 0
        for i in nums:
            if not m[i]:
                m[i] = m[i-1] + m[i+1]+1
                m[i-m[i-1]] = m[i]
                m[i+m[i+1]] = m[i]
            res= max(res,m[i])
        return res
                    