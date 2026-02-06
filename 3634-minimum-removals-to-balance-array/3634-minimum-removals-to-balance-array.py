class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        l=0
        for i in range(n):
            if nums[i]>k*nums[l]:l+=1
        return l