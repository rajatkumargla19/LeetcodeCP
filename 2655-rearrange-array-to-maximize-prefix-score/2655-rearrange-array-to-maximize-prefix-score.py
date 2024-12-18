class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # KABADA QUESTION THERE IS NO NEED TO WASTE TIME
        # Approach: sort the arr in decreasing order and then count the positives in the prefix_sum
        # My approach: first i have sorted arr then using a prefix_sum integer variable, I have checked from the last whether prefix_sum is negative at any stage then return res at the same stage.....
        # This soultion is O(nlogn) TC and O(1) space complexity.....
        nums.sort()
        n=len(nums)
        prefix_sum=0
        res=0
        for i in range(n-1,-1,-1):
            prefix_sum+=nums[i]
            if prefix_sum>0:res+=1
            if prefix_sum<0:
                return res
        return res