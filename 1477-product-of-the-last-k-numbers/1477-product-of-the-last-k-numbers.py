# Approach: O(1) time complexity and O(n) space complexity solution


class ProductOfNumbers:
    def __init__(self):
        self.prod=[]
        self.n=0
        self.lastpos=None
    def add(self, num: int) -> None:
        if num==0:
            self.lastpos=self.n
        if self.n==0:
            self.prod.append(num)
        elif self.n:
            if self.prod[-1]!=0:
                self.prod.append(self.prod[-1]*num)
            else:
                self.prod.append(num)
        self.n+=1
        


    def getProduct(self, k: int) -> int:
        # cases: [1] k==n [1.1] lastpos exist kare [1.2] lastpos exist na kare
        # cases 2: k<n [1.1] last se k+1th tak zero hai ya nahi hai ie; lastpos last se kth ke pahle hai ya baad me hai 
        # # pahle ye check kar ki last ke me koi zero to nahi hai 
        #    agar nahi hai to answer last se k+1th ke zero hone aur na hone pe depend karega
        #    agar zero hai to answer directly zero hoga...
        if k==self.n:
            # ye dhyan rakhna hai ki None and zero both value of lastpos
            # can be possible so handle them carefully
            if self.lastpos!=None:return 0
            return self.prod[-1];
        else:
            if not(self.lastpos) or self.lastpos<(self.n-k):
                return self.prod[-1]//(self.prod[-k-1] if self.prod[-k-1] else 1)
            return 0




        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)