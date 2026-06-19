class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for current in intervals[1:]:
            previous = result[-1]
            if current[0] <= previous[1]:
                result.pop(-1)
                result.append([min(previous[0], current[0]), max(previous[1], current[1])])
            else:
                result.append(current)

        return result
        