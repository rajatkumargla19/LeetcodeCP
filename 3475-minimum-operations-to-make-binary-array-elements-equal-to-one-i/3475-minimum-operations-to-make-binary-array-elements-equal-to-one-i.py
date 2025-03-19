class Solution:
    def minOperations(self, nums: List[int]) -> int:
        print(0==False)
        # return 3
        # # 1 0 0 1
        # # 1 1 1 0
        n=len(nums)
        res=0
        for i in range(n-2):
            if nums[i]==False:
                res+=1
                nums[i]=not(nums[i])
                nums[i+1]=not(nums[i+1])
                nums[i+2]=not(nums[i+2])
            else:
                continue
        for i in range(n):
            if not(nums[i]):return -1
        return res



        