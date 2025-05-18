class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        # res=-1
        for i in range(len(nums)):
            summ=0
            while nums[i]:
                summ+=nums[i]%10
                nums[i]//=10
            if summ==i:
                return i
        return -1

        