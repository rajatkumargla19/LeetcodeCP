class Solution:
    def binary(self,arr,n):
        #print(arr)
        lo=0
        hi=n-1
        while lo<=hi:
            mid=(lo+hi)//2
            if arr[mid]<0:
                if mid==0 or arr[mid-1]>=0:
                    return n-mid
                elif arr[mid-1]<0:
                    hi=mid-1
            elif arr[mid]>=0:
                lo=mid+1
        #print(0)
        return 0
    def countNegatives(self, grid: List[List[int]]) -> int:
        res=0
        m=len(grid)
        #print(m)
        n=len(grid[0])
        for i in range(m):
            #print(grid[i])
            res+=Solution().binary(grid[i],n)
            #print(res)
        return res
        