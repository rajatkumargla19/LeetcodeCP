class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        res=0
        i=2
        while i<n:
            left,right=0,i-1
            while left<right:
                if (nums[left] + nums[right]) > nums[i]:
                    res+=right-left
                    right-=1
                else:
                    left+=1
            i+=1
        return res
        