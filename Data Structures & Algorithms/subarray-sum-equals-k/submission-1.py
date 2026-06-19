class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_map = {0: 1}
        current_sum = 0
        result = 0
        for num in nums:
            current_sum += num

            if (current_sum - k) in prefix_sum_map:
                result += prefix_sum_map[current_sum - k]

            if current_sum in prefix_sum_map:
                prefix_sum_map[current_sum] += 1
            else:
                prefix_sum_map[current_sum] = 1

        return result
