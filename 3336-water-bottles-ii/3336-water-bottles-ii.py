class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full=0
        empty=numBottles
        drunkBottle=numBottles
        while empty+full>=numExchange:
            full+=1
            empty-=numExchange
            numExchange+=1
        return full+drunkBottle
        


    # 0 13 6 13
    # 1 7  7 13
    # 2 0  8 13
    # 0 2  8 15





      

        