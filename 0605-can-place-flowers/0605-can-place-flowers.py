class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m=len(flowerbed)
        if m==1:
            if flowerbed[0]==0:
                if n<=1:return True
                else:
                    return False
        for i in range(m):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
            elif i==m-1:
                if flowerbed[i-1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    n-=1
            else:
                if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                    n-=1
        return n<=0

            
        