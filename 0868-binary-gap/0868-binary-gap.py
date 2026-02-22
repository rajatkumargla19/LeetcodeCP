class Solution:
    def binaryGap(self, n: int) -> int:
        res=0
        first=0
        second=0
        i=1
        while n:
            if n%2:
                if not(first):first=i
                elif not(second):second=i
                else:
                    first=second
                    second=i
            res=max(res,second-first) if (first and second) else res
            n//=2
            i+=1
        # res=max(res,second-first) if (first and second) else res
        return max(res,second-first) if (first and second) else res
        