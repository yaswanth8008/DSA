# https://leetcode.com/problems/insert-interval/description/


def insert(intervals, newInterval):
    Output_intervals = []
    merged = None
    def NonOverlapping(interval_1,interval_2):
        if interval_1[0] > interval_2[1] or interval_2[0] > interval_1[1]:
            return True

    for i in range(len(intervals)):

        interval = intervals[i]
        if NonOverlapping(interval,newInterval):
            if merged == True:
                Output_intervals.append(interval)
            else:
                if min(interval[0],interval[1]) < min(newInterval[0],newInterval[1]):
                    Output_intervals.append(interval)
                else:
                    Output_intervals.append(newInterval)
                    newInterval = interval
          
        else:
            newInterval = [min(interval[0],newInterval[0]),max(interval[1],newInterval[1])]
            if i != len(intervals)-1:
                next_interval = intervals[i+1]
                if NonOverlapping(newInterval,next_interval):
                    
                    Output_intervals.append(newInterval)
                    merged = True
                    
            else:
                Output_intervals.append(newInterval)
                merged = True
            
    if merged != True:
        Output_intervals.append(newInterval)

    
    return Output_intervals