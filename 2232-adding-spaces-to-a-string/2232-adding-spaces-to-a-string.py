class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        n=len(s)
        x=0
        m=len(spaces)
        for i in range(n):
            if x<m and i!=spaces[x]:
                res.append(s[i])
            elif x==m:
                res.append(s[i])
            else:
                res.append(" ") 
                res.append(s[i])
                x+=1
        print(res)
        return "".join(res)
        