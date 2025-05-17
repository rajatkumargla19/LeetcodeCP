class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0,0,0,0,0,1,1,1,1,1,2,2,2]
        i=0
        n=len(nums)
        j=n-1 # [0, 0, 2i, 1, 1, 2]
        while i<j:
            while i<j and nums[i]==0:
                i+=1
            while i<j and nums[j]!=0:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        i=0
        j=n-1
        while i<j:
            while i<j and nums[i]!=2:
                i+=1
            while i<j and nums[j]!=1:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        return nums


        

        