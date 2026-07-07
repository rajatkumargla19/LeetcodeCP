class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res=0
        while n:
            res=(10*res+n%10) if n%10 else res
            n//=10
        sm=0
        x=0
        while res:
            x=10*x+res%10
            sm+=res%10  
            res//=10 
        # print(x,sm)
        return x*sm
        