class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        for i in range(n):
            if i!=n-1 and prices[i+1]>prices[i]:
                res+=prices[i+1]-prices[i]
        return res