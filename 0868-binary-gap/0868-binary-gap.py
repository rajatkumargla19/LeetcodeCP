class Solution:
    def binaryGap(self, n: int) -> int:
        res=0
        # 10110
        first=0
        second=0
        i=1
        while n:
            if n%2:
                if not(first):
                    first=i #2
                elif not(second):
                    second=i #3
                else:
                    first=second
                    second=i
            res=max(res,second-first) if (first and second) else res
            n//=2
            i+=1
        res=max(res,second-first) if (first and second) else res
        return res
        