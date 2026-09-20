class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        i = 1
        n = len(intervals)
        while i<n:
            if intervals[i][0]<=end:
                if intervals[i][1]>end:
                    end = intervals[i][1]
            else:
                res.append([start,end])
                start = intervals[i][0]
                end = intervals[i][1]
                interval = [start,end]
            i+=1
        res.append([start,end])
        return res
