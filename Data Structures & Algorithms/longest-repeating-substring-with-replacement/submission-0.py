class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26
        maxCount = 0
        start = 0
        for end in range(len(s)):
            counter[ord(s[end]) - ord('A')] += 1
            maxCount = max(maxCount, counter[ord(s[end]) - ord('A')])

            if end - start + 1 - maxCount > k:
                counter[ord(s[start]) - ord('A')] -= 1
                start += 1
        
        return end - start + 1