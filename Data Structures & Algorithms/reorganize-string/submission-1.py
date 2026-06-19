class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = []
        for c, freq in counter.items():
            heapq.heappush(heap, (-freq, c))
        
        result = ""
        while len(heap) > 1:
            freq1, c1 = heapq.heappop(heap)
            freq2, c2 = heapq.heappop(heap)
            result += c1
            result += c2
            if freq1 + 1 < 0:
                heapq.heappush(heap, (freq1 + 1, c1))
            if freq2 + 1 < 0:
                heapq.heappush(heap, (freq2 + 1, c2))

        if heap:
            freq, c = heap[0]
            if -freq > 1:
                return ""
            result += c
        return result