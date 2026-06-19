class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # racecar
        # carrace
        # r: 2, a: 2, c: 2, e: 1
        # c: 2, a: 2, r: 2, e: 1
        # [1, 1, 0, 0, 0...1]
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        
        return True
