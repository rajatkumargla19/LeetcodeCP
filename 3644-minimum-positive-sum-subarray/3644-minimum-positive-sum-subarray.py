class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res=float('inf')
        current_sum=0
        n=len(nums)
        prefix_sum=[0]*n
        prefix_sum[0]=nums[0]
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        # print(prefix_sum)
        i=0
        j=i+l-1
        while i+l-1<n:
            current_sum=prefix_sum[j]-(prefix_sum[i-1] if i>0 else 0)
            if current_sum>0:res=min(res,current_sum)
            if j-i+1==r:
                i+=1
                j=i+l-1
            else:
                if j+1==n:
                    i+=1
                    j=i+l-1
                else:
                    j+=1
        return res if res!=float('inf') else -1
                
            

