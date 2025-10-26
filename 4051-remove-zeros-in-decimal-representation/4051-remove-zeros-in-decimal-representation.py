class Solution:
    def removeZeros(self, n: int) -> int:
        res=0
        x=0
        while n:
            if n%10:
                res+=(10**x)*(n%10)
                x+=1
            n//=10
            
        return res