class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2

            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(float(pile) / mid)
            if totalHours <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res