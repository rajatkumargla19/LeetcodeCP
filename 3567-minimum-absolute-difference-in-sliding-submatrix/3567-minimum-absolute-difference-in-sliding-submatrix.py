class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row=len(grid);
        col=len(grid[0]);
        res=[[0 for i in range(col-k+1)] for j in range(row-k+1)];
        # print(res)
        for i in range(row-(k-1)):
            for j in range(col-(k-1)):
                min_diff=float('inf')
                curr_diff=float('inf')
                mat=[]
                for r in range(i,i+k):
                    for c in range(j,j+k):
                        mat.append(grid[r][c])
                mat.sort()
                print(mat)
                for x in range(1,len(mat)):
                    if mat[x]!=mat[x-1]:
                        curr_diff=mat[x]-mat[x-1]
                    min_diff=min(min_diff,curr_diff)
                if min_diff!=float('inf'):
                    res[i][j]=min_diff
                # print(min_diff)
        return res;




        

        