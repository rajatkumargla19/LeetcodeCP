class Solution:
    def numTilings(self, n: int) -> int:
        # there is a pattern for this problem and that is T(n)=2*T(n-1)+T(n-3)
        # it is just like fibonacci series and memoization is required fof the same...
        # 1D memoization is enough to solve this problem...
        if n<3:
            return n
        # memo=[1 for i in range(n+1)]
        # memo[2]=2
        thirdprev=1
        secondprev=1
        prev=2

        for i in range(3,n+1):
            current=(2*prev+thirdprev)%(10**9+7)
            temp=prev
            prev=current
            temp2=secondprev
            secondprev=temp
            thirdprev=temp2
        return (current)%(10**9+7)

            






        