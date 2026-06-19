class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i, num in enumerate(nums):
            if (target - num) in nmap:
                return nmap[target - num], i
            nmap[num] = i
