class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        average=sum(candies)//k
        n=len(candies)
        lo=1
        hi=average
        ans=0
        while lo<=hi:
            mid=(lo+hi)//2
            mid_possible=0
            for i in candies:
                mid_possible+=i//mid
            if mid_possible>=k:
                lo=mid+1
                ans=mid
            else:
                hi=mid-1;
        return ans
            

        



        