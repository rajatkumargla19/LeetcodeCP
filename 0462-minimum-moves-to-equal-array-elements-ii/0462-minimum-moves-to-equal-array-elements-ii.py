class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        mean=nums[n//2]
        res=0
        for i in range(n):
            res+=abs(mean-nums[i])
        return res
        # 1 2 9 10
