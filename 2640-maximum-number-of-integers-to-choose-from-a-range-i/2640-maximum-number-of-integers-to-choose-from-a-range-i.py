class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.sort()
        count=0
        def search(arr,target):
            low,high =0,len(banned)-1
            while low<=high:
                mid=low+(high-low)//2
                if arr[mid]==target:return True
                elif arr[mid]>target:high=mid-1
                else:low=mid+1
            return False
        for i in range(1,n+1):
            if maxSum>=i and not(search(banned,i)):
                maxSum-=i
                count+=1
        return count
