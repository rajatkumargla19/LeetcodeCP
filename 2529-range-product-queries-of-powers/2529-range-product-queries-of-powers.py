import math
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        pp=[]
        while n:
            digits=int(math.log2(n)+1)
            pp.append(2**(digits-1))
            n-=pp[-1]
        pp=pp[::-1]
        ln=len(pp)
        prefix=[pp[0]]
        i=1
        mod=10**9+7
        while i<ln:
            prefix.append((prefix[-1]*pp[i]))
            i+=1
        
            
        print(prefix)
        
        res=[]
        ln=len(queries)
        for i in range(ln):
            curr=prefix[queries[i][1]]
            prev=prefix[queries[i][0]-1] if (queries[i][0]>0) else 1 
            mod=(10**9+7)
            res.append((curr//prev)%mod )
        return res
        return []


        