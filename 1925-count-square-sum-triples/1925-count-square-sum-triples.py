class Solution:
    def countTriples(self, n: int) -> int:
        # return 5
        # 1 2 3 4
        res=0
        for i in range(1,n):
            for j in range(1,n):
                if (i**2+j**2)<=n**2 and int((i**2+j**2)**0.5)==((i**2+j**2)**0.5):
                    res+=1
        return res
        