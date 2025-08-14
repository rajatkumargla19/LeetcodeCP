import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n=-8
        # return True
        return False if n<=0 else (True if int(math.log2(n))==math.log2(n) else False)
        
        