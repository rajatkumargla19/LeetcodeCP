class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        i=n-2
        if n==1:
            if nums[0]>k:return 1
            elif nums[0]==k:return 0
            return -1
        res=0
        while i>=0:       # 2 4 5 *5 5 ... 
            if nums[i]==nums[i+1]:
                i-=1
            else:
                res+=1
                # print(res,'index=',i); 
                i-=1
        if nums[0]==k: 
            return res
        elif nums[0]>k:
            return res+1
        return -1

            
