class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res=[]
        n=len(nums)
        i=0
        j=n//2
        for i in range(n//2):
            res.append(nums[i])
            res.append(nums[j])
            j+=1
        return res