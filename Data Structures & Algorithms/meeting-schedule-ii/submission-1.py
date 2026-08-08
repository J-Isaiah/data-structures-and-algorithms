"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        max_count = 0
        count = 0
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        
        starts.sort()
        ends.sort()

        start = 0
        end = 0

        while start < len(intervals):
            if starts[start] < ends[end]:
                start += 1 
                count += 1 
                max_count = max(max_count, count)
            elif starts[start] > ends[end]:
                end += 1 
                count -= 1 
                max_count = max(max_count, count)
            else:
                count -= 1
                end +=1
                max_count = max(max_count, count)


        return max_count




