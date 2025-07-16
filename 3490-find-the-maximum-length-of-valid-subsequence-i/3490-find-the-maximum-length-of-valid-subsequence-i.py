class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        oddsSeq=0
        diffparitySeq=1
        n=len(nums)
        for i in range(n):
            if nums[i]%2:
                oddsSeq+=1
            if i!=0:
                if nums[i]%2!=nums[i-1]%2:
                    diffparitySeq+=1
        return max(oddsSeq,n-oddsSeq,diffparitySeq)

            


        