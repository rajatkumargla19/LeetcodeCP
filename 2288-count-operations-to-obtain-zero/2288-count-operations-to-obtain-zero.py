class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # (2,3)
        # (2,1)
        # (1,1)
        # (0,1)
        # return 2
        res=0
        while num1!=0 and num2!=0:
            if num1>=num2:
                num1-=num2
            else:
                num2-=num1
            res+=1
        return res


        