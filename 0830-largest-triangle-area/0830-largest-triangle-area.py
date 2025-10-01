class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxarea=0
        n=len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    x1,x2,x3=points[i][0],points[j][0],points[k][0]
                    y1,y2,y3=points[i][1],points[j][1],points[k][1]
                    area=0.5*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
                    maxarea=max(maxarea,area)
        return maxarea
        