class Solution:
    def flowerGame(self, n: int, m: int) -> int:
         return ( ((m+1)//2) *(n//2) ) + ( (m//2) *((n+1)//2) )

        