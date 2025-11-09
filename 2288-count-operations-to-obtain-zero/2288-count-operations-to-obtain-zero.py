class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # (2,3)
        # (2,1)
        # (1,1)
        # (0,1)
        # return 2
        res=0
        if num1==0 or num2==0:return 0
        if num1>=num2 and num1%num2==0:return num1//num2
        if num2>num1 and num2%num1==0:return num2//num1
        while num1 and num2:
            if num1>=num2:
                res+=num1//num2
                num1=num1%num2
            else:
                res+=num2//num1
                num2=num2%num1
            # print(num1,num2)
        return res
       



        