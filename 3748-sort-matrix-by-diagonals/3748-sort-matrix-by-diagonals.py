class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        for j in range(1,n):
            row,col=0,j
            temp=[]
            # while loop for extracting elements of each diagonal and storing them into temp for sorting purposes
            while row<m and col<n:
                temp.append(grid[row][col])
                row,col=row+1,col+1
            temp.sort()
            # print(temp)
            row,col=0,j
            # while loop for placing the extracted elements back into the diagonal of the grid
            while row<m and col<n:
                grid[row][col]=temp[row]
                row,col=row+1,col+1
        #Symmetric code for placing the elements of the lower matrix elements back to the grid
        for i in range(0,m):
            row,col=i,0
            temp=[]
            # while loop for extracting the lower half one by one 
            while row<m and col<n:
                temp.append(grid[row][col])
                row,col=row+1,col+1
            temp=sorted(temp)[::-1]
            row,col=i,0
            # print(temp)
            # while loop for putting the extracting elements back to the grid again
            while row<m and col<n:
                grid[row][col]=temp[col];
                row,col=row+1,col+1
        return grid






        