class Solution:

    def __init__(self, w: List[int]):
        self.length = len(w)
        s = sum(w)
        self.weights = []
        for num in w:
            self.weights.append(num / s)

    def pickIndex(self) -> int:
        options = [i for i in range(self.length)]
        return random.choices(options, self.weights, k = 1)[0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()