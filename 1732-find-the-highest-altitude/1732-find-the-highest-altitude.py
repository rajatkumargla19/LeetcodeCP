class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=0
        n=len(gain)
        ans=float("-inf")
        for i in range(n):
            gain[i]+=res
            res=gain[i]
            if gain[i]>ans:
                ans=gain[i]
        if ans>0:
            return ans
        return 0
        
        
        