class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # summ=(n*(n+1))//2
        # m+2m+3m+4m=m(1+2+3+...)
        # (1+2+3)*m=18
        summ=(n*(n+1))//2
        dividend=n//m
        all_divisibleByM=((dividend*(dividend+1))//2)*m
        return summ-2*all_divisibleByM
        
        