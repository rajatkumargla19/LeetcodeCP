class Solution:
    def digit_sum(self,n):
        res=0
        while n:
            res+=n%10
            n//=10
        return res
    def minElement(self, nums: List[int]) -> int:
        min_res=float('inf')
        for i in range(len(nums)):
            nums[i]=Solution().digit_sum(nums[i])
            if nums[i]<min_res:
                min_res=nums[i]
        return min_res

        