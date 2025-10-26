class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # nums.sort()
        n=len(nums)
        for i in range(n):
            nums[i]=abs(nums[i])
        nums.sort(reverse=True)
        print(nums)
        half=(len(nums)+1)//2
        print(half)
        res=0
        i=0

        while i<n:
            if i<half:
                res+=nums[i]**2
            else:
                res-=nums[i]**2
            i+=1
        return res
