class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        for i in range(len(n)):
            if nums[i]>k*nums[l]:l+=1
        return l