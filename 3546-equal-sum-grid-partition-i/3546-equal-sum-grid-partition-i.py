class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rowwise_sum=[]
        colwise_sum=[]
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            row_sum=0
            for j in range(col):
                row_sum+=grid[i][j]
            rowwise_sum.append(row_sum)
        for i in range(col):
            col_sum=0
            for j in range(row):
                col_sum+=grid[j][i]
            colwise_sum.append(col_sum)
        # print(rowwise_sum)
        # print(colwise_sum)
        # return True
        prefix_rowwise=[rowwise_sum[0]]
        prefix_colwise=[colwise_sum[0]]
        for i in range(1,row):
            prefix_rowwise.append(prefix_rowwise[-1]+rowwise_sum[i])
        for i in range(1,col):    
            prefix_colwise.append(prefix_colwise[-1]+colwise_sum[i])
        print(prefix_rowwise)
        print(prefix_colwise)
        for i in range(row):
            if prefix_rowwise[-1]==2*prefix_rowwise[i]:
                return True
        for i in range(col):
            if prefix_colwise[-1]==2*prefix_colwise[i]:
                return True
        return False
        



        
        