class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Approach: This question is simple two pointer based question....Alice has also choice to 
        # take and not take .... so he will always win
        return True
        n=len(piles)
        i=0
        j=n-1
        Alice,Bob=0,0
        turn=True
        while i<=j:
            if turn:
                if piles[i]>=piles[j]:
                    Alice+=piles[i]
                    i+=1
                else:
                    Alice+=piles[j]
                    j-=1
            
            else:
                if piles[i]>=piles[j]:
                    Bob+=piles[i]
                    i+=1
                else:
                    Bob+=piles[j]
                    j-=1
            turn=not(turn)
        print(Alice,Bob)
        return Alice>Bob

        
        