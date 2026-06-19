class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        maxHeap = []
        for task, count in counter.items():
            heapq.heappush(maxHeap, -count)
        
        time = 0
        queue = []
        while maxHeap or queue:
            time += 1

            if not maxHeap:
                time = queue[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    queue.append([count, time + n])
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.pop(0)[0])
        return time
            