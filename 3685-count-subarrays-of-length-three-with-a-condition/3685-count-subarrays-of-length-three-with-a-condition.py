class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=2
        count=0
        while i+2<n:
            if 2*(nums[i]+nums[j])==nums[i+1]:count+=1
            i+=1
            j+=1
        return count
        