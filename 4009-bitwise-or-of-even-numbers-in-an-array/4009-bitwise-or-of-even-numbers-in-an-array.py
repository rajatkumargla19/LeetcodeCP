class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        # return [1|nums[i] for i in range(len(nums)) if nums[i]%2==0]
        res=0
        for i in range(len(nums)):
            res=res|nums[i] if nums[i]%2==0 else res
        return res
        