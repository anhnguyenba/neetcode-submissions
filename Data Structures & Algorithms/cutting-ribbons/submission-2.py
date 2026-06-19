class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 0, max(ribbons)
        while left < right:
            mid = (left + right + 1) // 2
            if sum([ribbon // mid for ribbon in ribbons]) >= k:
                left = mid
            else:
                right = mid - 1
        
        return left
