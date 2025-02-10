


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        output_intervals = []
        intervals.sort(key=lambda x: (x.start,x.end))
        new_interval = intervals[0]
        
        for i in range(1,len(intervals)):
            i = intervals[i]
            if i.start <= new_interval.end:
                new_interval.start = min(i.start,new_interval.start)
                new_interval.end = max(i.end,new_interval.end)
            else:
                dummy_interval = Interval(new_interval.start,new_interval.end)
                output_intervals.append(dummy_interval)
                new_interval.start = i.start
                new_interval.end = i.end

        output_intervals.append(new_interval)
        return output_intervals