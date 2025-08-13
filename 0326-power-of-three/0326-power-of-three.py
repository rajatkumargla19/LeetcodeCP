import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:return False
        temp=math.log(n,3)
        temp = round(temp, 10)

        print(temp)
        return True if temp==int(temp) else False