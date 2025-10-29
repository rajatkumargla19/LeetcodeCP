import math
class Solution:
    def smallestNumber(self, n: int) -> int:
        digits=int(math.log2(n)+1)
        # print(digits)
        return 2**(digits)-1
        
        