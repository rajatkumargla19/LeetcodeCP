class Solution:
    def longestPrefix(self, s: str) -> str:
        res=''
        length=0
        n=len(s)
        print(s[n-1:])
        for i in range(1,n):
            if s[:i]==s[n-i:]:
                res=s[:i]
        return res
        