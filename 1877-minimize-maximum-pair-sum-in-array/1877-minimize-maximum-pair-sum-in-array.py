class Solution:
    def minPairSum(self, nums: List[int]) -> int:
    #    [2,3,3,5]
    #    [2,3,4,4,5,6]
        nums.sort()
        i=0
        j=len(nums)-1
        max_pair_sum=float('-inf')
        while i<j:
            max_pair_sum=max(max_pair_sum,nums[i]+nums[j])
            i+=1
            j-=1
        return max_pair_sum
