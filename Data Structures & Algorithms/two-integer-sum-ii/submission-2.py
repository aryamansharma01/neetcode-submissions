class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(len(numbers)):
            l = i+1
            r = n-1
            while l<=r:
                mid = l+(r-l)//2
                if numbers[mid]==target-numbers[i]:
                    return [i+1,mid+1]
                elif numbers[mid]>target-numbers[i]:
                    r = mid-1
                else:
                    l = mid+1
        return []
