class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        
        most=[nums[0],1]
        for i in freq:
            if freq[i]>most[1]:
                most=[i,freq[i]]
        count=0
        for i in range(n):
            if nums[i]==most[0]:
                count+=1 
                if count*2>(i+1) and (most[1]-count)*2>(n-i-1):
                    return i

        return -1






        


        