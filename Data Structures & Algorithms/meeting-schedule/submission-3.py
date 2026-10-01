"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True 

        intervals.sort(key=lambda i: i.start)
        lastEnd = intervals[0].end
        ans = True 

        for i in range(1, len(intervals)):

            start = intervals[i].start
            end = intervals[i].end
            if lastEnd <= start:
                lastEnd = end 
            else:
                return False 
        
        return ans
                



