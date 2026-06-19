class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def backtrack(i, curr_sum):
            if curr_sum == target:
                res.append(comb.copy())
                return
            if i >= len(nums) or curr_sum > target:
                return
            
            comb.append(nums[i])
            backtrack(i, curr_sum + nums[i])

            comb.pop()
            backtrack(i + 1, curr_sum)

        backtrack(0, 0)
        return res