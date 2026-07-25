class Solution:
    def maxProduct(self, n: int) -> int:
        a=0
        b=0
        while n:
            mod=n%10
            if mod>a:
                b=a
                a=mod
            elif mod>b:
                b=mod
            n//=10
        return a*b