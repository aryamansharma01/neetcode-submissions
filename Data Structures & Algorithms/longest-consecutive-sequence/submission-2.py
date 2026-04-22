class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest, length = 0,0
        for i in nums:
            if i-1 not in s:
                length = 1
                while i+length in s:
                    length+=1
            longest = max(length, longest)
        return longest