class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        # [8 4 2 30 15]
        # [4 8 2 30 15]
        # [4 2 8 30 15 ]
        # [1 1 1 4 4]

        # [2 1 1 1 1]
        # [3 2 4 8 16]
        # [1 1 2 1 2]
        # two pointer+sorting question+ set bit count...
        def set_bit_count(x):
            count=0
            while x:
                count+=1 if x%2 else 0
                x//=2
            return count
        n=len(nums)
        if n==1:return True
        temp=[0]*n 
        for i in range(n): 
            temp[i]=set_bit_count(nums[i])
        # print(temp) 
        i=0
        j=i+1
        while j<=n:
            if j<n and temp[i]==temp[j]: 
                j+=1
            elif j<n:           
                nums[i:j]=sorted(nums[i:j]) 
                # print(sorted(nums[i:j])) 
                i=j  
                j=i+1  
            else:
                nums[i:j]=sorted(nums[i:j])
                j+=1
            

        # print(nums)
        for i in range(1,n):
            if nums[i-1]>nums[i]:return False
        return True

