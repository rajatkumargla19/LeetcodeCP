class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        sm=sum(nums)
        res=float('-inf')
        suffixMin=float('inf')
        n=len(nums)
        for i in range(n-1,0,-1):
            sm-=nums[i]
            suffixMin=min(suffixMin,nums[i])
            res=max(res,sm-suffixMin)
        return res
        