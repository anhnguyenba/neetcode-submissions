class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, curr_sum, comb):
            if curr_sum == target:
                res.append(comb.copy())
                return
            if i >= len(candidates) or curr_sum > target:
                return
            
            comb.append(candidates[i])
            backtrack(i + 1, curr_sum + candidates[i], comb)
            comb.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr_sum, comb)
        
        backtrack(0, 0, [])
        return res