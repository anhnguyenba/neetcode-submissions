class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        sub = []

        def backtrack(i):
            if i >= len(nums):
                subsets.append(sub.copy())
                return
            
            sub.append(nums[i])
            backtrack(i + 1)

            sub.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return subsets