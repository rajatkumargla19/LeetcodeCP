class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        # mp={}
        # n=len(candyType)
        # count=0
        # for i in range(n):
        #     if candyType[i] not in mp:
        #         mp[candyType[i]]=1
        #         count+=1
            
        # if count<n//2:
        #     return count
        # return n//2
        return min(len(set(candyType)),len(candyType)//2)