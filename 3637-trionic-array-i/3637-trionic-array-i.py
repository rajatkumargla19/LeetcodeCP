class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if nums[0]>=nums[1]:return False
        increasing=0
        decreasing=0
        n=len(nums)
        flag=False
        for i in range(1,n):
            if nums[i-1]==nums[i]:return False 
            if nums[i-1]<nums[i] and not(flag):
                increasing+=1
                flag=not(flag)
            elif nums[i-1]>nums[i] and flag: 
                decreasing+=1
                flag=not(flag)
            # if :return False


        return (increasing==2 and decreasing==1)

            # [1,2,3,4]
            # 2 1 3
            # 8 9 4 6 1
            # inc=11
            # dec=1

        