class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1
        streak = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                streak += 1
            elif nums[i] != nums[i - 1]:
                streak = 1
            res = max(res, streak)
        return res
