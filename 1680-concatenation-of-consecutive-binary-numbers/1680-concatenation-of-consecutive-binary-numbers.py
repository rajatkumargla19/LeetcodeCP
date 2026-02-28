class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res=0
        m=10**9+7
        for i in range(1,n+1):
            digit=int(math.log2(i)+1)
            res=((res<<digit)%m+i)%m
        return res%m

        