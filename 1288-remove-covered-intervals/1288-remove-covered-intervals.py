class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        print(intervals)
        st=[]
        i=0
        res=n
        while i<n:
            if not(st):st.append(intervals[i])
            elif st[-1][0]==intervals[i][0] and st[-1][1]<=intervals[i][1]:
                st.pop()
                st.append(intervals[i])
                res-=1
            elif st[-1][1]>=intervals[i][1]:
                res-=1
            else:
                st.append(intervals[i])
            i+=1
        return res
        