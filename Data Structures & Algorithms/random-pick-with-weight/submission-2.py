import bisect

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = [0]
        for num in w:
            self.prefix.append(self.prefix[-1] + num)
        self.prefix.pop(0)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix[-1])
        return bisect.bisect_left(self.prefix, target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()