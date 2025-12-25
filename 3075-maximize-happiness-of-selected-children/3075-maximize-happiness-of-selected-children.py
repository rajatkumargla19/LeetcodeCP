class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        # [1 2 3]
        # selected=3
        # i=last
        # count=1
        # [1 1 1 1]
        # k=2
        # [2 3 4 5] k=1
        happiness.sort()
        i=len(happiness)-1
        count=0
        res=0
        while i>=0:
            if k>0 and happiness[i]-count>0:
                res+=happiness[i]-count
                i-=1
                k-=1
                count+=1
            else:
                return res   
        return res 
        # 50+6+1
