class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        streak=0
        res=0
        for i in range(len(nums)):
            streak=streak+1 if nums[i]==0 else 0
            res+=streak
        return res
        