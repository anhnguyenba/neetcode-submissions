class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        while low < high:
            val = (low + high) // 2
            if nums[val] < target:
                low = val + 1
            elif nums[val] > target:
                high = val
            else:
                return val
        
        return -1
