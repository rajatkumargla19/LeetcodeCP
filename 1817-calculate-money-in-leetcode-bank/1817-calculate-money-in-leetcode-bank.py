class Solution:
    def totalMoney(self, n: int) -> int:
        # 1 2 3 4 5 6 7   1+2+3+4+5 6 7 + 0*days
        # 2 3 4 5 6 7 8.. 1 2 3 4 5 6 7 + 1*days
        # 3 4 5 6 7 8 9 ..1,2,3,4,5,6,7 + 2*days
        # Approach 1
        # x=0
        # res=0
        # while n>0:
        #     if n>7:
        #         res+=(28+x*7)
        #     else:
        #         res+=(n*(n+1))//2+x*n
        #     n-=7
        #     x+=1
        # return res
        # # 28 , 35+ 21+12
        # Approach 2: O(1) time
        r=n%7
        d=n//7
        f=d*(d-1)//2
        # return (d*28)+ (7*(f if d else 0)) + (r*(r+1))//2+ d*r 
        return d*28 + 7*f + (r*(r+1))//2 + d*r             
        


        