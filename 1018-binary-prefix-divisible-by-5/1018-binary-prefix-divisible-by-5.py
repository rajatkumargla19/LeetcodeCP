class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n=len(nums)
        current_num=0
        res=[]
        for i in range(len(nums)):
            current_num=current_num*2+nums[i]
            # print(current_num)
            res.append(current_num%5==0)
        return res
