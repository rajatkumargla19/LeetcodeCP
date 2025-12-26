class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        prefix=[0]*(n+1)
        suffix=[0]*(n+1)
        # prefix=[0,0,0,1,1]
        # suffix=[3,2,1,1,0]
        for i in range(n):
            prefix[i+1]=prefix[i]+(1 if customers[i]=='N' else 0)
            suffix[n-i-1]=suffix[n-i]+(1 if customers[n-i-1]=='Y' else 0)
        res=float('inf')
        res_idx=float('inf')
        for i in range(n+1):
            if prefix[i]+suffix[i]<res:
                res=prefix[i]+suffix[i]
                res_idx=i
        return res_idx
            
