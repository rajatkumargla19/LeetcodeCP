class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        temp=x+k-1 # last wali row ko each time track karne ke liye we took temp
        for i in range(x,x+k//2):
            # x ko x+k//2 tak hi lekar jana hai yani half tak hi, kyoki next half ke saath to isko swap karna hi hai.. unko kyo lenge...
            for j in range(y,y+k):
                # grid me ek row ko end wali row se swap karna hai, this is the crux of this easy problem
                grid[i][j],grid[temp][j]=grid[temp][j],grid[i][j]
            # ek baar swapping ho jaane par temp ko upper wali row ko point karna hai, so we are 
            # reducing it by 1... 
            temp-=1
        return grid


        