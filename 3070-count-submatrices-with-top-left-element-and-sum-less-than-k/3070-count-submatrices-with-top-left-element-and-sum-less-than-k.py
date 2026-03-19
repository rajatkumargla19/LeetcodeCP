class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        row=len(grid)
        col=len(grid[0])
        mat=[[0 for i in range(col)] for j in range(row)]
        count=0
        # colm wise addition
        for i in range(col):
            for j in range(row):
                mat[j][i]=(mat[j-1][i] if j>0 else 0)+grid[j][i]
        # now row-wise addition
        for i in range(row):
            for j in range(col):
                if j>0:
                    mat[i][j]+=mat[i][j-1]
                if mat[i][j]<=k:count+=1
        # for i in range(row):
        #     for j in range(col):
        #         if mat[i][j]<=k:
        #             count+=1
        return count


         
        

        