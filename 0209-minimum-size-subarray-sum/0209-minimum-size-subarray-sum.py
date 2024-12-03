class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # [2 5 6 8 12i 15j]
        
        n=len(nums)
        prefix_sum=[0]*n
        prefix_sum[0]=nums[0]
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]

        # CORNER CASE: when total sum of prefix sum array is less than target
        if target>prefix_sum[-1]:return 0
        i=0
        j=0
        res=float('inf')
        # This loop is used just to make the adjustable window only... 
        # whose length can be adjusted according to the current window sum
        while j<n:
            if (prefix_sum[j]-(prefix_sum[i-1] if i>0 else 0))>=target:
                res=min(res,j-i+1)
                # decreasing the current window length as sum is greater than or equal to the target
                i+=1
            else:
                # as the window sum is lesser than the target, so increasing the length of the window
                j+=1
        return res





            








        
        