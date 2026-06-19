import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        current_sum = 0
        for num in w:
            current_sum += num
            self.prefix.append(current_sum)
        self.total = current_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()