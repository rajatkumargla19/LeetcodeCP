class Solution:
    def xor_sum(self,p):
        res=0
        for i in p:
            res^=i
        return res

    def sxs(self,up,p):
        if len(up)==0:
            return Solution().xor_sum(p)
        ch=up[0]
        left=Solution().sxs(up[1:],p+[ch])
        right=Solution().sxs(up[1:],p)
        return left+right

    def subsetXORSum(self, nums: List[int]) -> int:
        return Solution().sxs(nums,[])


        
        