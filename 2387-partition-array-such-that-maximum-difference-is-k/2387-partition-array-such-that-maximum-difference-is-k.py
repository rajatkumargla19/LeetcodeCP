class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=1
        n=len(nums)  # [1,2,3,5,6]
        # temp=[]
        start=nums[0]
        for i in range(1,n):
            # if not(temp):
            #     start=nums[i]
            if nums[i]-start>k:
                count+=1
                start=nums[i]
        return count
                



        