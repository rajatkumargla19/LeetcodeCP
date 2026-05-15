class Solution:
    def findMin(self,arr:List[int])->int:
        lo=0
        n=len(arr)
        hi=n-1
        while lo<=hi:
            mid=(lo+hi)//2
            if mid+1<n and arr[mid]>arr[mid+1]:
                return arr[mid+1]
            elif arr[mid]>arr[n-1]:
                lo=mid+1
            else:
                hi=mid-1
        return arr[0]
    