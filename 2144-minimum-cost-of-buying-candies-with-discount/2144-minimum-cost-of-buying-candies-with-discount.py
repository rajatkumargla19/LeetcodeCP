class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # [2,2,5,6,(7,9)]
        # return 5
        cost.sort()
        res=0
        n=len(cost)
        i=n-1
        while i>=0:
            if i>=0:
                res+=cost[i]
            if i-1>=0:
                res+=cost[i-1]
            i=i-3
        return res
        # [2,2,5,6,7,9]




