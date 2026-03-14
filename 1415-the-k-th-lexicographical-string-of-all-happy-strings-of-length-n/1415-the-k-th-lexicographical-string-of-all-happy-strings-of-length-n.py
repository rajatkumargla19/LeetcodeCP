class Solution:
    def happy(self,p,up,n,k,res):
        if len(p)==n:
            res.append(p)
            return 
        for j in range(3):
            if not(p) or (p[-1]!=up[j]):
                Solution().happy(p+up[j],up,n,k,res)
        return res
        
    def getHappyString(self, n: int, k: int) -> str:
        res=Solution().happy('','abc',n,k,[])
        # print(res)
        return res[k-1] if len(res)>=k else ""
        