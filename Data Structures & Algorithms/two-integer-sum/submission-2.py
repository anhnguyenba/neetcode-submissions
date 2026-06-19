class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for i, num in enumerate(nums):
            if target - num in sum_map:
                return [sum_map[target - num], i]
            sum_map[num] = i
