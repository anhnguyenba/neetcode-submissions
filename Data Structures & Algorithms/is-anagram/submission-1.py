class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter_count = [0] * 26
        for c in s:
            letter_count[ord(c) - ord('a')] += 1
        
        for c in t:
            letter_count[ord(c) - ord('a')] -= 1
        
        for i in range(26):
            if letter_count[i] > 0:
                return False

        return True