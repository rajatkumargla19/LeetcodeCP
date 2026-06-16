class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        n=len(s)
        for i in range(n):
            if s[i]=="*":
                if res:
                    res.pop()
            elif s[i]=="#":
                res=res*2
            elif s[i]=="%":
                res=res[::-1]
            else:
                res.append(s[i])
        return "".join(res)



        