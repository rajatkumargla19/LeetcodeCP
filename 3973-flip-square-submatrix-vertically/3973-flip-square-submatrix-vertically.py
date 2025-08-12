class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        temp=x+k-1
        for i in range(x,x+k//2):
            for j in range(y,y+k):
                grid[i][j],grid[temp][j]=grid[temp][j],grid[i][j]
            temp-=1
        return grid


        