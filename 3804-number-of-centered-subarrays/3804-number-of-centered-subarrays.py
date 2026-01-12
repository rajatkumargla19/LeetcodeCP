class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for start in range(n):
            running_sum = 0
            elements_set = set()
            for end in range(start, n):
                running_sum += nums[end]
                elements_set.add(nums[end])
                if running_sum in elements_set:
                    res += 1
        return res