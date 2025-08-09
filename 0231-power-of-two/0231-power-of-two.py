class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        if int(n)!=n:
            return False
        elif n==1:
            return True
        return Solution().isPowerOfTwo(int(n)/2)