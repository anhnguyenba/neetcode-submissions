class MedianFinder:

    def __init__(self):
        # max heap
        self.small = []
        # min heap
        self.large = []

    def addNum(self, num: int) -> None:
        # [3, 2] | []
        # [2] | [3] (balance)
        # [2, 1] | [3]
        # [2, 1] | [3, 4]
        # median = (2 + 3) // 2
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-1 * self.small[0] + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return -1 * self.small[0]
        else:
            return self.large[0]
        