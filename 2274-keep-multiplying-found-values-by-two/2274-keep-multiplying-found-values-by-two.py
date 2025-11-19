class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        if original not in d:
            return original
        while True:
            if 2*original not in d:
                return 2*original
            else:
                original*=2
        