class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        map={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in map:
                map[nums[i]]=1
            else:
                map[nums[i]]+=1
        i=0
        count=0
        res=0
        if len(map)==n:return res
        while i<n:
            count=0
            while count<3 and i+count<n:
                map[nums[i+count]]-=1
                if map[nums[i+count]]==0:del map[nums[i+count]]
                count+=1

            res+=1
            if len(map)==n-i-3:return res
            i+=3

        return res 

