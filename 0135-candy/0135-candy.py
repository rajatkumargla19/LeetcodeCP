class Solution:
    def candy(self, ratings: List[int]) -> int:
        # # [1,2,2,1,3,2,1,1,2]
        #   [1,2,2,1,3,2,1,1,2]
        n=len(ratings)
        res=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                if res[i]<=res[i-1]:
                    res[i]=res[i-1]+1
        print(res)
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                if res[i]<=res[i+1]:
                    res[i]=res[i+1]+1
        print(ratings)
        return sum(res)
        