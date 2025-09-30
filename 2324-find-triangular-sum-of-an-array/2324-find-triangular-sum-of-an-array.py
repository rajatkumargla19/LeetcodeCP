class Solution:
    def triangularSum(self,nums:List[int])->int:
        #1 2 3 4j 5
        #3 5 7 9 5
        n=len(nums)
        for i in range(n):
            for j in range(0,n-i-1): 
                nums[j]=(nums[j]+nums[j+1])%10
                
                
        print(nums) 
        return nums[0]
    #[1 2 3 4 5]
    #[3 5 7 9 5]
    
    
    
            
    