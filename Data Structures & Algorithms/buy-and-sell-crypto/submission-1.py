class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        l = 0
        r = 1
        while r<n:
            if prices[r]>prices[l]:
                profit = max(prices[r]-prices[l],profit)
            elif prices[r]<prices[l]:
                l = r
            r+=1
        return profit

