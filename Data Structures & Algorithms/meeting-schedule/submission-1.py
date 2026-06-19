"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        count = len(intervals)
        if count == 0 or count == 1:
            return True
        intervals.sort(key=lambda x: x.start)
        previous = intervals[0]
        for current in intervals[1:]:
            if current.start < previous.end:
                return False
            previous = current
        return True
