class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, tem in enumerate(temperatures):
            while stack and tem > stack[-1][0]:
                t, index = stack.pop()
                res[index] = i - index
            stack.append((tem, i))
        
        return res        
