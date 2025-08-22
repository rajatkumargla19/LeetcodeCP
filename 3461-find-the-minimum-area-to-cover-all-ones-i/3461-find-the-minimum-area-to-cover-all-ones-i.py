class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        # row=[0,1]
        # col=[0,2]
        # (2-0+1)*(1-0+1)=3*2=6
        row_expand=[float('inf'),float('-inf')]
        col_expand=[float('inf'),float('-inf')]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    row_expand[0]=min(row_expand[0],i)
                    # row_expand[1]=max(row_expand[1],i)
                    row_expand[1]=i
                    col_expand[0]=min(col_expand[0],j)
                    col_expand[1]=max(col_expand[1],j)
        # print(row_expand)
        # print(col_expand)
        return (row_expand[1]-row_expand[0]+1)*(col_expand[1]-col_expand[0]+1)
        # 0
        # 1
