class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # return 3
        mp={}
        n=len(candyType)
        for i in range(n):
            if candyType[i] not in mp:
                mp[candyType[i]]=1
            else:
                mp[candyType[i]]+=1
        print(mp)
        # return n//2
        if len(mp)<n//2:
            return len(mp)
        return n//2