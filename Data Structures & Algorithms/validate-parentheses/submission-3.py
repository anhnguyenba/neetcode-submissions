class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { ')': '(', '}': '{', ']': '[' }
        stack = []
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif c in [')', '}', ']']:
                if not stack or stack[-1] != brackets[c]:
                    return False
                stack.pop(-1)
        
        return len(stack) == 0
        