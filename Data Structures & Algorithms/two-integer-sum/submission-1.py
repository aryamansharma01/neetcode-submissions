class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, n in enumerate(nums):
            dict[n] = i
        for i,n in enumerate(nums):
            diff = target-n
            if diff in dict and dict[diff]!= i:
                return [i, dict[diff]]
        return []