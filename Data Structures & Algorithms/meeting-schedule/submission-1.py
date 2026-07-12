"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda t:t.start)
        for i in range(1,len(intervals)):
            priormeeting=intervals[i-1]
            currentmeeting=intervals[i]
            if priormeeting.end>currentmeeting.start:
                return False
        return True