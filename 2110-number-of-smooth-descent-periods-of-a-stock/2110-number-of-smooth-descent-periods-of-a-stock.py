class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        [1,2,3]
        # 1 2 3 12 123 23...
        # Approach: sliding window type question only
        i=0
        j=1
        res=0
        n=len(prices)
        while i<n:
            if j>=n:break
            if prices[j-1]-prices[j]==1:
                j+=1
            else:
                diff=j-i
                res+=(diff*(diff+1))//2
                i=j
                j=i+1
        res+=((j-i)*(j-i+1))//2
        return res





        