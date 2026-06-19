class Solution:
    def _merge(self, interval1: List[int], interval2: List[int]) -> List[int]:
        return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        N = len(intervals)

        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        if newInterval[1] == intervals[0][0]:
            return [self._merge(newInterval, intervals[0])] + intervals[1:]
        
        if newInterval[0] == intervals[-1][1]:
            return intervals[:N-1] + [self._merge(intervals[-1], newInterval)]

        result = []
        left, right = None, None

        for i in range(N):
            if newInterval[0] <= intervals[i][1]:
                left = i
                break
        
        for i in range(N - 1, -1, -1):
            if newInterval[1] >= intervals[i][0]:
                right = i
                break

        result = []
        for i in range(left):
            result.append(intervals[i])
        
        result.append([min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])])

        for i in range(right + 1, N):
            result.append(intervals[i])
        
        return result
