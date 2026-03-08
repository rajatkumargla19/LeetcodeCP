class Solution:
    def func(self,p,up,d,k):
        if len(p)==k:
            if p not in d:
                return p
            else:
                return ''
        left=Solution().func(p+'0',up,d,k)
        right=Solution().func(p+'1',up,d,k)
        if left:
            return left
        if right:
            return right
        
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
        return Solution().func('','01',d,len(nums[0]))