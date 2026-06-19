class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {3: 3, 2: 2, 1: 1}
        # k = 2: 3, 2
        # dict + heap

        # Build a counter dict
        # Loop through dict: add (count, value) to a maxheap
        # Loop 0 -> k - 1: pop the top of the heap, add to the result

        # Time complexity: O(klogN) with N is the number of unique numbers.
        # Space complexity: O(N)

        # We could use a heap of size k to reduce the time complexity to O(klogk) = O(1)
        # while len(heap) > k: heapq.heappop(heap)
        # result = [value for _, value in heap]
        heap = []
        counter = Counter(nums)
        for num, count in counter.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [value for _, value in heap]