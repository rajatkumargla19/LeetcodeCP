class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # return 2
        sm=sum(nums)
        n=len(nums)
        sum_so_far=0
        res=0
        # if 
        for i in range(n):
            if nums[i]==0:
                if sum_so_far==sm-sum_so_far:
                    res+=2
                elif (sum_so_far==sm-sum_so_far-1) or (sum_so_far==sm-sum_so_far+1):
                    res+=1
            else:
                sum_so_far+=nums[i]
        return res
            
        