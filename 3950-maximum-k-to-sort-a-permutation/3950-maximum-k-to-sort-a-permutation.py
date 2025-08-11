class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        # wrongpos=[]
        n=len(nums)
        res=(2**32)-1
        for i in range(n):
            if nums[i]!=i:
                res&=nums[i]
        return res if res!=((2**32)-1) else 0   
        