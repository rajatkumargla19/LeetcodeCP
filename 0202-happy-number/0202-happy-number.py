class Solution:
    def isHappy(self, n: int) -> bool:
        res=0
        num_so_far={n:1}

        while True:
            if n**2<10:
                if n==1:
                    return True
                return False
            
            while n>0:
                res+=(n%10)**2
                n//=10
            if res in num_so_far:
                return False
            else:
                num_so_far[res]=1
            
            n=res
            res=0
            # print(n)
            