class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=abs(nums[i])
        nums.sort(reverse=True)
        half=(len(nums)+1)//2
        res,i=0,0
        while i<n:
            res=(res+nums[i]**2) if i<half else (res-nums[i]**2)
            i+=1
        return res

