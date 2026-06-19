class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar
        # carrace
        # r: 2, a: 2, c: 2, e: 1
        # c: 2, a: 2, r: 2, e: 1
        # [1, 1, 0, 0, 0...1]
        char_array = [0] * 26
        for c in s:
            char_array[ord(c) - ord('a')] += 1
        
        for c in t:
            val = char_array[ord(c) - ord('a')]
            if val == 0:
                return False
            char_array[ord(c) - ord('a')] -= 1
        
        return sum(char_array) == 0
