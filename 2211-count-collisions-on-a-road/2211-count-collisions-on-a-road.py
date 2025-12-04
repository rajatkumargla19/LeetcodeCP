class Solution:
    def countCollisions(self, directions: str) -> int:
        n=len(directions)
        i=0
        while i<n and directions[i]=='L':i+=1
        j=n-1
        while j>=0 and directions[j]=='R':j-=1
        res=0
        while i<=j:
            if directions[i]!='S':
                res+=1
            i+=1
        return res
