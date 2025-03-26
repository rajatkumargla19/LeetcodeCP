class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # 2 4 6 8
        temp=[]
        row=len(grid)
        col=len(grid[0])
        for i in range(row):
            for j in range(col):
                temp.append(grid[i][j])
        temp.sort()
        print(temp)
        n=len(temp)
        mean=temp[n//2]
        # 1 2 2 1000
        res=0
        for i in range(n):
            if abs(mean-temp[i])%x:return -1
            res+=abs(mean-temp[i])//x
            # print(res)
        return res
