class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # I can do this question with the help of two pointers for sliding window + maintaining the prefix sum arr for calculating the varying sum of the current subarr........
        n=len(nums)
        if n==1:
            return nums[0]
        prefix_sum=[nums[0]];
        for i in range(1,n):
            prefix_sum.append(prefix_sum[-1]+nums[i])
        print(prefix_sum)
        res=0
        temp=0
        mp={nums[0]:0}
        i=0
        j=1
        while j<n:
            if nums[j] not in mp:
                # temp+=nums[j]
                mp[nums[j]]=j;
            else:
                res=max(res,prefix_sum[j-1]-(prefix_sum[i-1] if i-1>=0 else 0))
                # print(res)
                if i<=mp[nums[j]]:
                    i=mp[nums[j]]+1
                mp[nums[j]]=j

            j+=1
        # 5i,2,1,2j,5,2,1,2,5  # 4 2i 4 5 6j
        # mp={4:2,2:1,5:3,6:4}

        return max(res,prefix_sum[j-1]-(prefix_sum[i-1] if i-1>=0 else 0))









        