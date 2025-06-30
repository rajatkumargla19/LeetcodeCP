class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n=len(nums)
        freq={}
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        res=0
        for i in freq:
            predecessorORsuccessor=max( (freq[i-1] if i-1 in freq else 0),(freq[i+1] if i+1 in freq else 0) )
            res=max(res, freq[i]+predecessorORsuccessor if predecessorORsuccessor else 0 )
        return res
        