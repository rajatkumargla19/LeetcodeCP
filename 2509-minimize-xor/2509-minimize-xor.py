import math
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
            n1_digits=int((math.log2(num1))+1)
            n2_setbits=0
            while num2:
                n2_setbits+=num2%2
                num2//=2
            res=[]
            setbits=n2_setbits
            while n2_setbits>0 and n1_digits>0:
                if num1 & (1<<(n1_digits-1)):
                    res.append(1)
                    n2_setbits-=1
                else:
                    res.append(0)
                n1_digits-=1
            while n1_digits:
                res.append(0)
                n1_digits-=1
            length=len(res)
            index=length-1
            if n2_setbits:
                while n2_setbits and index>=0:
                    if res[index]==0:
                        res[index]=1
                        n2_setbits-=1
                    index-=1
            if length<setbits:
                res.extend([1]*(setbits-length))
            
            # print(res)
            
            # calculating length again as in above if condition the actual length of the res has increasing dues to extend funcition used
            length=len(res)
            x=0
            for i in range(length-1,-1,-1):
                x+=1<<(length-i-1) if res[i] else 0
            return x
            





        