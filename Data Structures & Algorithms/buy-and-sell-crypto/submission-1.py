class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        start = 0
        for end in range(1, len(prices)):
            while prices[end] < prices[start] and start < end:
                start += 1
            res = max(res, prices[end] - prices[start])
        return res

        