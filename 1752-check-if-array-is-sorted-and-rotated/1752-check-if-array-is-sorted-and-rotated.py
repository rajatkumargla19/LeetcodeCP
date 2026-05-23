class Solution:
    def check(self, nums: List[int]) -> bool:
        turns=0;
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                turns+=1
        print(turns)
        if nums[-1]>nums[0]:turns+=1
        print(turns)
        return turns<=1


        