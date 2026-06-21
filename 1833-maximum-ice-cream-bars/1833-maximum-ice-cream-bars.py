class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        # [1,1,2,3,5,6]
        costs.sort()
        i=0
        n=len(costs)
        icecreams=0
        while i<n and costs:
            if coins-costs[i]>=0:
                coins-=costs[i]
                icecreams+=1
                i+=1
            else:
                break
        return icecreams

        