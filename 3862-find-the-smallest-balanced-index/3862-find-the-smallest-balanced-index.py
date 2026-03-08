class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        res,n=-1,len(nums)
        prefix_sum=[nums[0]]
        for i in range(1,n):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        prod=1
        for i in range(n-1,0,-1):
            if prefix_sum[i-1]==prod:res=i
            if prefix_sum[n-1]<prod:break
            prod*=nums[i]
        return res