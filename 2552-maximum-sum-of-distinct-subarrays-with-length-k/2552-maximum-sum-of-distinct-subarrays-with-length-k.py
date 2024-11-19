class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        # *algo: take a set for adding unique number into it and checking whether current state of set contains the k number of elements or not?
        # at the same time , find prefix_sum for the nums arr
        # [1 6 10 12 21 30 39]
        prefix_sum=[0]*n
        prefix_sum[0]=nums[0]
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+nums[i]
        d={}
        res=0 
        #  [ 1 5 4 2 9 9 9]
        #    [1 6 10 19 28 37]
        for i in range(k):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        # print(d)
        if len(d)==k:
            res=prefix_sum[k-1]
        for i in range(k,n):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
            
            if d[nums[i-k]]>1:
                d[nums[i-k]]-=1
            else:
                del d[nums[i-k]];
            # print(d)
            if len(d)==k:
                res=max(res,prefix_sum[i]-prefix_sum[i-k])
        return res


