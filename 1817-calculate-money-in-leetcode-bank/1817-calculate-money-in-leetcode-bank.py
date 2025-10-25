class Solution:
    def totalMoney(self, n: int) -> int:
        # 1 2 3 4 5 6 7   1+2+3+4+5 6 7 + 0*days
        # 2 3 4 5 6 7 8.. 1 2 3 4 5 6 7 + 1*days
        # 3 4 5 6 7 8 9 ..1,2,3,4,5,6,7 + 2*days

        x=0
        res=0

        while n>0:
            if n>7:
                res+=(28+x*7)
            else:
                res+=(n*(n+1))//2+x*n
            n-=7
            x+=1
        return res
        # 28 , 35+ 21+12



        


        