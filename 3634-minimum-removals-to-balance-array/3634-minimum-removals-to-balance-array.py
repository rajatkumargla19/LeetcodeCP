class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        res=0
        i=0
        j=i
        while j<n:
            if (k*nums[i])>=nums[j]:
                j+=1
            else:
                print(i,j)
                res=max(res,j-i) # [1 2 6i 9j] 2
                # print(res)
                i+=1
        res=max(res,j-i)
        return n-res
        