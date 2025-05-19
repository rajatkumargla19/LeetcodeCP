class Solution:
    def triangleType(self, nums: List[int]) -> str:
        maxx=max(nums)
        summ=sum(nums)
        if maxx>=(summ-maxx):return 'none'
        if nums[0]!=nums[1] and nums[1]!=nums[2] and nums[0]!=nums[2]:return "scalene"
        if nums[0]==nums[1] and nums[1]==nums[2]:return "equilateral"
        return "isosceles"

        
        