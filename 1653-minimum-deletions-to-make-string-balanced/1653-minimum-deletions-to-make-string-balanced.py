class Solution:
    def minimumDeletions(self, s: str) -> int:
        ass=0
        bss=0
        n=len(s)
        res=0
        for i in range(n):
            if s[i]=='b':
                bss+=1
            elif s[i]=='a' and bss:
                res+=1
                bss-=1
        return res


                    



        