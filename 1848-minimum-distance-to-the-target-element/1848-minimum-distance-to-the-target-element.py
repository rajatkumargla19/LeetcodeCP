class Solution:
    # def bs(arr,target,lo,hi):
    #     mid=(lo+hi)//2
    #     while lo<=hi:
    #         if arr[mid]==target or ((mid>0 and arr[mid-1]<target) and (mid<n-1 and arr[mid+1]>target)):




    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        # [0,1,2,8,5,6,7,8,9]
        freq=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==target:
                freq.append(i)
                
        m=len(freq)
        res=float('inf')
        for i in range(len(freq)):
            res=min(res,abs(freq[i]-start))
        return res
        
        

        
        