class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        x_grid=[[0 for i in range(col)] for j in range(row)]
        y_grid=[[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="X":
                    x_grid[i][j]=(x_grid[i][j-1]+1) if j>0 else 1
                    y_grid[i][j]=y_grid[i][j-1] if j>0 else 0  
                elif  grid[i][j]=="Y":
                    y_grid[i][j]=(y_grid[i][j-1]+1) if j>0 else 1
                    x_grid[i][j]=x_grid[i][j-1] if j>0 else 0
                else:
                    x_grid[i][j]=x_grid[i][j-1] if j>0 else 0
                    y_grid[i][j]=y_grid[i][j-1] if j>0 else 0
        # print(y_grid)
        for j in range(col):
            for i in range(1,row):
                x_grid[i][j]+=x_grid[i-1][j]
                y_grid[i][j]+=y_grid[i-1][j]
        # print(x_grid);
        # print(y_grid)
        # return 4
        res=0     
        for i in range(row):
            for j in range(col):
                if (x_grid[i][j] and y_grid[i][j]) and x_grid[i][j]==y_grid[i][j]:res+=1
        return res
# [0,1,1,1]
# [1,1,1,1]
# [0,0,1,1]
# [0,0,0,1]
# added
# [0,1,1,1]
# [1,2,1,1]
# [1,2,3,3]
# [1,2,3,4]
