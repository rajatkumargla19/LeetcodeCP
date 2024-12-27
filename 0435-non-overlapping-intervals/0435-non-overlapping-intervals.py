class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        intervals.sort()

        i=0
        j=1
        n=len(intervals)
        while j<n:
            if intervals[i][1]>intervals[j][0]:
                if intervals[i][1]>intervals[j][1]:
                    i=j
                j+=1
                count+=1
            else:
                i=j
                j=i+1
        return count
                    

        