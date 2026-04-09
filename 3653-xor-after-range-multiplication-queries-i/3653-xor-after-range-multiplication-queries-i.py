class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        n=len(nums)
        q=len(queries)
        mod=10**9+7
        for i in range(q):
            l=queries[i][0]
            r=queries[i][1]
            s=queries[i][2]
            v=queries[i][3]
            while l<=r:
                nums[l]=(nums[l]*v)%mod
                l+=s
        print(nums)
        # return 10
        res=0
        for i in range(n):
            res^=nums[i]
        return res


        