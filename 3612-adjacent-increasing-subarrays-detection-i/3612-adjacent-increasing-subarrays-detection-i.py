class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        inc=1
        prevInc=0
        maxLen=0
        n=len(nums)
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                inc+=1
            else:
                prevInc=inc
                inc=1
            if inc>=2*k or (inc>=k and prevInc>=k):return True
            
        return False

        


    

