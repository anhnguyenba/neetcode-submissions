import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        cache = dict()
        
        def dfs(i: int):
            if i == len(intervals):
                return 0
            
            if i in cache:
                return cache[i]

            # skip the job
            res = dfs(i + 1)

            # take the job
            j = bisect.bisect_left(intervals, (intervals[i][1], -1, -1))
            
            res = max(res, intervals[i][2] + dfs(j))
            cache[i] = res
            return res

        return dfs(0)