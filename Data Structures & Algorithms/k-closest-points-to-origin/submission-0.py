class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points):
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (-distance, i))
            while len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for d, i in heap:
            res.append(points[i])
        return res
        