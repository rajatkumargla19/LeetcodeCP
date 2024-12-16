import heapq as hq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # nums=[6,1,1,5,1]
        temp=[[nums[i],i] for i in range(len(nums))]
        # print(temp)
        hq.heapify(temp)
        # print(temp)
        while k:
            top=hq.heappop(temp)
            nums[top[1]]*=multiplier
            hq.heappush(temp,[nums[top[1]],top[1]])
            k-=1
        # print(nums)
        # print(temp)
        return nums
        