class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        # [10 14 6 13]
#         # [2 5* 6* 6]
#         This logic is good: 
# as total of the arr is equal to the sum, and if left_subarr has sum more than half of the total sum then right_subarr sum will definetely will be lesser than the left subarr sum so following code is based on awesome observation of the coder.... following code is a single traversal logic of the problem 
# This logic has O(1) space complexity and single traversal code so it is very efficient than prefix sum wala code logic.....
        n=len(nums)
        prefix=[nums[0]]
        for i in range(1,n):
            prefix.append(prefix[-1]+nums[i])
        # print(prefix)
        res=0
        for i in range(n-1):
            if prefix[i]>=prefix[-1]-prefix[i]:res+=1
        return res

