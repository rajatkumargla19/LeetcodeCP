class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        inc=1
        prevInc=0
        res=1
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                inc+=1
            else:
                prevInc=inc
                inc=1
            # res=max(res, ((inc+1)//2, min(inc,prevInc)))
            res=max(res, max(inc//2,min(inc,prevInc)))
            
        return res       
        