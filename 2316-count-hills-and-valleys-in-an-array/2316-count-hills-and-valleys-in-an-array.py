class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        left = nums[0]        
        count = 0
        n=len(nums)
        for i in range(1,n-1):
            if nums[i] != nums[i + 1]:
                if (left < nums[i] > nums[i + 1]) or (left > nums[i] < nums[i + 1]):
                    count += 1
                left = nums[i]
        return count


        