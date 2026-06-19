class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # nee((t(c)o())de)
        stack = []
        remove = set()
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                if stack:
                    stack.pop(0)
                else:
                    remove.add(i)
    
        result = ""
        stack = set(stack)
        for i, c in enumerate(s):
            if i not in remove and i not in stack:
                result += c
        
        return result