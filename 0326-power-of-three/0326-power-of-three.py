class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        largest=3**19
        return True if (n>0 and largest%n==0) else False