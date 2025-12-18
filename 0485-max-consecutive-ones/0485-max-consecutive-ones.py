class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        track_zero=-1
        res=0
        n=len(nums)
        for i in range(n):
            if nums[i]==0:
                # track_zero=i
                if track_zero==-1:
                    res=max(res,i)
                else:
                    res=max(res,i-track_zero-1)
                track_zero=i
        if track_zero==-1:
            return n
        return max(res,n-track_zero-1)

        