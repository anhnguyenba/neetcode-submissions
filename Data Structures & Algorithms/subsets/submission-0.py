class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(index, sub):
            if index <= len(nums) - 1:
                subsets.append(list(sub))
            
            for i in range(index + 1, len(nums)):
                sub.append(nums[i])
                backtrack(i, sub)
                sub.remove(nums[i])
        
        backtrack(-1, [])
        return subsets