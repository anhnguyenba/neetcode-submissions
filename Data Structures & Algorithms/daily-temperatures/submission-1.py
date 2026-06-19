class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [0]
        # [1] 1
        # [1, 2]
        # [1, 3, 4]   
        # min stack
        stack = []
        result = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                result[stack[-1]] = i - stack[-1]
                stack.pop(-1)
            stack.append(i)
        return result
