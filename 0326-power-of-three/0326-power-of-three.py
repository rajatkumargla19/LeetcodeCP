class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0 or int(n)!=n:
            return False
        elif n==1:
            return True
        return Solution().isPowerOfThree(n/3)