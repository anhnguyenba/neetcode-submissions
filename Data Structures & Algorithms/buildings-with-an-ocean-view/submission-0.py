class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] <= height:
                stack.pop(-1)
            stack.append(i)
        
        return stack