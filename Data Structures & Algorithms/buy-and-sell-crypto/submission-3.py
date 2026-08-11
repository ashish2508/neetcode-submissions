class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = prices[0]
        fpr = 0

        for i in range(1, len(prices)):
            mn = min(mn, prices[i])
            fpr = max(fpr, prices[i] - mn)

        return fpr