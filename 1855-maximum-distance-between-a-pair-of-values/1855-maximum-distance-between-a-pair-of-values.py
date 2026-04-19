class Solution:
    def binary(self,arr2,n2,target):
        lo=0
        hi=n2-1
        while lo<=hi:
            m=(lo+hi)//2
            if arr2[m]>=target and (m+1==n2 or (m+1<n2 and arr2[m+1]<target)):return m
            elif arr2[m]>=target:
                lo=m+1
            else:
                hi=m-1
        return -1
    def maxDistance(self,arr1: List[int], arr2: List[int]) ->int:
        res=0
        n1=len(arr1)
        n2=len(arr2)
        for i in range(n1):
            x=Solution().binary(arr2,n2,arr1[i])
            #print(x,end=" ")
            if (x-i)>res:
                res=(x-i)
        return res
            