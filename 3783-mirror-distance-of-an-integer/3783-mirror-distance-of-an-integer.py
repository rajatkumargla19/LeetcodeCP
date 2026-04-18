class Solution:
    def mirrorDistance(self, n: int) -> int:
        res=n
        rev=0
        while n:
            rev=rev*10+n%10
            n//=10
        print(rev,res)
        return abs(res-rev)
