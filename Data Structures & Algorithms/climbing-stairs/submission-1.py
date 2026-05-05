class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        prev1 = 3
        prev2 = 2
        for i in range(4,n+1):
            curr = prev1+prev2
            prev2 = prev1
            prev1 = curr
        return curr

        