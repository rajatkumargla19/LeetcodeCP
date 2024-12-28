class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m=len(flowerbed)
        if m==1:
            if flowerbed[0]==0:
                if n<=1:return True
                else:
                    return False
        i=0
        while i<m:
            # flag is used for last i increment whether we have to increment i by 1 or by 2...
            flag=0
            # corner case 1
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1

                    flag=1
                    n-=1
            # corner case 2
            elif i==m-1:
                if flowerbed[i-1]==0 and flowerbed[i]==0:
                    flowerbed[i]=1
                    n-=1

                    flag=1
            else:
                if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0:
                    flowerbed[i]=1
                   
                    flag=1
                    n-=1
            # i+=2 bcz if current element is satisfying the condition then the next element is not going to satisfy the same 
            # so there is no point in checking the next element,so we are going to check  the +2 element 
            # this is just a simple optimization, nothing else...
            if flag:
                i+=2
            else:
                i+=1
            # This is for checking when n is equal to zero so there is no point in checking further 
            # as we can do the operation n time successfully and this is the only requirement
            if not(n):return True
        return n<=0

            
        