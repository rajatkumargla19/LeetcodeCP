import heapq as hq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        temp=[[nums[i],i] for i in range(len(nums))]
        hq.heapify(temp)
        # print(temp)
        score=0
        n=len(nums)
        while temp:
            if nums[temp[0][1]]>0:
                if temp[0][1]>0 and nums[temp[0][1]-1]>0:
                    nums[temp[0][1]-1]*=(-1) ;
                if temp[0][1]<n-1 and nums[temp[0][1]+1]>0:
                    nums[temp[0][1]+1]*=(-1) ;
                score+=temp[0][0]
                nums[temp[0][1]]*=(-1) ;
            hq.heappop(temp)
        # nums=[-2,-1,-3,-4,-5,-2]
        

        return score


        