class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        f0=0
        for i in range(n):
            f0+=i*nums[i]
        prev,res=f0,f0

        arr_sum=sum(nums)
        for i in range(n-1,0,-1):
            prev=prev+arr_sum-n*nums[i]
            res=max(res,prev)
            # prev=curr
        return res

        