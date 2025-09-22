class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq={}
        max_freq=0
        n=len(nums)
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]]=1

            else:
                freq[nums[i]]+=1
            max_freq=max(max_freq,freq[nums[i]])
        print(freq)
        print(max_freq)
        res=0
        for i in freq:
            if freq[i]==max_freq:
                res+=max_freq
        return res
        
        