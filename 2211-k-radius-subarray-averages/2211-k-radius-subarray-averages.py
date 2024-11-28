class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        prefix_sum=[0]*n
        prefix_sum[0]=prefix_sum[0]
        for i in range(n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        res=[-1]*n
        for i in range(k,n-k):
            res[i]=(prefix_sum[i+k]-(prefix_sum[i-k-1] if i-k>0 else 0))//(2*k+1)
        return res
        