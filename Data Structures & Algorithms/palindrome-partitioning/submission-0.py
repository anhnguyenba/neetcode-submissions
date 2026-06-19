class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []

        def isPalindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(parts.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    parts.append(s[i:j + 1])
                    backtrack(j + 1)
                    parts.pop()
        
        backtrack(0)
        return res