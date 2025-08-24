class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:return 0
        interval=[]
        i=0
        j=i
        
        while i<n and j<n:
            while i<n and nums[i]==0: 
                i+=1
            
            if i<n:
                j=i+1
            else:
                break
            # j=i+1
            while j<n and nums[j]==1:
                j+=1
            interval.append([i,j-1])
            i=j
        # print(interval)
        res=1
        li=len(interval)
        if li==0:return 0
        elif li==1:
            if (interval[0][1]-interval[0][0]+1)<n:
                return interval[0][1]-interval[0][0]+1;
            return interval[0][1]-interval[0][0];
        res=interval[0][1]-interval[0][0]+1;
        for i in range(1,li):
            if (interval[i][0]-interval[i-1][1])==2:
                res=max(res,interval[i][1]-interval[i-1][0]);
            else:
                res=max(res,interval[i][1]-interval[i][0]+1)
        return res;


            
        