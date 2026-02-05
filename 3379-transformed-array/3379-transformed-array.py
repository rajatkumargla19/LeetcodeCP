class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(n):
            res.append( nums[(i+nums[i])%n])
            # elif nums[i]<0:
            #     res.append()
            # [5,-2,6,1]
            # []
        return res


        return res
        