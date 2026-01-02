class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        res=0
        if (cost1+cost2>costBoth):
            res+=min(need1,need2)*costBoth
            if need1>need2:res+=(need1-need2)*min(cost1,costBoth)
            else:res+=(need2-need1)*min(cost2,costBoth)
            return res
        else:return need1*cost1+need2*cost2