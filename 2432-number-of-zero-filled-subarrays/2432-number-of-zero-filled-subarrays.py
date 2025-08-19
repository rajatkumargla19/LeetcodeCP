class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        # count=0
        res=0
        while i<n and nums[i]!=0:
            i+=1
        if i<n and nums[i]==0:
            count=1
            j=i+1
        if i==n:
            return res
        while j<n:
            if nums[j]==0:
                j+=1
                count+=1
            else:
                res+=(count*(count+1))//2
                i=j+1
                j+=1
                count=0
        if count:
            res+=(count*(count+1))//2
        return res
        