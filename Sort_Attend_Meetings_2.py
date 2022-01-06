def can_attend_all_meetings(intervals):
    
    #if its all sorted; just need to check ith end interval vs i+1's start
    
    #nested_list = [[2, "c"], [1, "b"], [3, "a"]]
    sorted_list = sorted(intervals, key=lambda x: x[0])
    
    
    for i in range(len(sorted_list)-1):
        if sorted_list[i][1] > sorted_list[i+1][0]:
            return 0
    
    return 1

XXXXXXXXX

def can_attend_all_meetings(intervals):
    sorted_ints = sorted(intervals, key=lambda x : x[0])
    
    for i in range(1, len(sorted_ints)):
        if sorted_ints[i-1][1] > sorted_ints[i][0]:
            return 0
    
    return 1

XXXXXXXXX

def can_attend_all_meetings(intervals):
    
    for i in range(len(intervals)-1):
        if intervals[i][1] >  intervals[i+1][0] and intervals[i][0] <  intervals[i+1][1]:
            return 0 
    
    return 1         


XXXXXXXXX

def can_attend_all_meetings(intervals):
    for indx in range(len(intervals)-1):
        ary1 = intervals[indx]
        ary2 = intervals[indx + 1]

        if (ary2[0] < ary1[1] and ary2[1] > ary1[0]):
            return 0
    return 1
    
XXXXXXXXX

def can_attend_all_meetings(intervals):
    sortIntervals = sorted(intervals, key=lambda a:a[0])
    end_first = sortIntervals[0][1]
    for i in range(1, len(sortIntervals)):
        end_second = sortIntervals[i][0]
        if end_first > end_second:
            return 0
        end_first = sortIntervals[i][1]
    return 1