class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        for j in range(1,n):
            row,col=0,j
            temp=[]
            while row<m and col<n:
                temp.append(grid[row][col])
                row,col=row+1,col+1
            temp.sort()
            print(temp)
            row,col=0,j
            while row<m and col<n:
                grid[row][col]=temp[row]
                row,col=row+1,col+1
        # now the next symmetric code comes
        for i in range(m):
            row,col=i,0
            temp=[]
            while row<m and col<n:
                temp.append(grid[row][col])
                row,col=row+1,col+1
            temp=sorted(temp)[::-1]
            row,col=i,0
            print(temp)
            while row<m and col<n:
                grid[row][col]=temp[col]
                row,col=row+1,col+1
        return grid






        