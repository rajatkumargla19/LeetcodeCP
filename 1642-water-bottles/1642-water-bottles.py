class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty=0
        res=numBottles
        while numBottles>=numExchange:
            res+=numBottles//numExchange
            empty=numBottles%numExchange
            numBottles=numBottles//numExchange+empty
        return res


            