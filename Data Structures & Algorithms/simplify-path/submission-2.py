import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        # c == '..'
        # c == '/'
        # neetcode, practice, /..., //, .., courses
        # stack = [neetcode, practice, ..., courses]
        path_components = path.split("/")
        stack = []
        for comp in path_components:
            if stack and comp == '..':
                stack.pop(-1)
            elif comp not in ['..', '.', '']:
                stack.append(comp)
        
        return "/" + "/".join(stack)

        
