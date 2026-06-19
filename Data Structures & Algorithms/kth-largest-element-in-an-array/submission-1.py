class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap = []
        # heap = [1, 2, 3] -> [2, 3]
        # heap = [2, 3, 5] -> [3, 5]
        # heap = [3, 4, 5] -> [4, 5]
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            while len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]