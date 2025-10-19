class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # [ 1-k,2-(k),2-k || 3+1,3+2,4+1,4+2 ]
        
        #  [ 1,1,1  ||  1,1,1 ] 
        nums.sort()
        cnt=0
        prev=float('-inf');
        for num in nums:
            curr=min(max(num-k,prev+1),num+k);
            if curr>prev:
                cnt+=1
                prev=curr
        return cnt








        