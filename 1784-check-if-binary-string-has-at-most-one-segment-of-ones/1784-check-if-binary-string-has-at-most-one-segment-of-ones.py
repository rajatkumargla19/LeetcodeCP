class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        zero,one,n=0,0,len(s)
        for i in range(n):
            if s[i]=='1' and (not(i) or s[i-1]=='0'):
                one+=1
        return one==1 

        