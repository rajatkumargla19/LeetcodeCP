class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count=0
        i=0
        res=[]
        n=len(s)
        for j in range(n):
            count=(count+1) if (s[j]=='1') else (count-1)
            if not(count):
                res.append('1'+Solution().makeLargestSpecial(s[i+1:j])+"0")
                i=j+1
        res.sort(reverse=True)
        return "".join(res)

        