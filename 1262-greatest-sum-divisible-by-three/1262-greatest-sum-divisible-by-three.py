class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sm=sum(nums)
        if sm%3==0:return sm
        rem1=[]
        rem2=[]
        n=len(nums)
        for i in range(n):
            if nums[i]%3==1:
                rem1.append(nums[i])
            elif nums[i]%3==2:
                rem2.append(nums[i])
        rem1.sort()
        rem2.sort()
        rem=sm%3
        if rem==1:
            result1=float("inf") if len(rem1)==0 else  rem1[0] 
            result2=float("inf") if len(rem2)<=1 else  rem2[0]+rem2[1]
            result=min(result1,result2)
        elif rem==2:
            result1=float('inf') if len(rem1)<=1 else  rem1[0]+rem1[1]
            result2=float('inf') if len(rem2)==0 else rem2[0]
            result=min(result1,result2)
        
        return sm-result
        