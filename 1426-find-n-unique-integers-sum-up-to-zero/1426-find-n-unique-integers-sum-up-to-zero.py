class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [-(n*(n-1)//2)]+[i for i in range(1,n)]

        