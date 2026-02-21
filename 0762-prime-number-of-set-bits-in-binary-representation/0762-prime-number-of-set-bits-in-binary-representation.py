class Solution:
    def countSetBits(self,x):
        setBits=0
        while x:
            if x%2:
                setBits+=1
            x//=2
        print(setBits)
        return setBits
    def isprime(self,x):
        if x==2: return True
        if x<2 or x%2==0:return False
        for i in range(3,int(sqrt(x)+1),2):
            if x%i==0:return False
        return True
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        while left<=right:
            if Solution().isprime(Solution().countSetBits(left)):res+=1
            left+=1
        return res
