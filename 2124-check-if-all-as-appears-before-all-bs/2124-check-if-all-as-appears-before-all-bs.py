class Solution:
    def checkString(self, s: str) -> bool:
        bss=False
        for i in range(len(s)):
            if s[i]=='b':bss=True
            if s[i]=='a' and bss:return False
        return True
        
        