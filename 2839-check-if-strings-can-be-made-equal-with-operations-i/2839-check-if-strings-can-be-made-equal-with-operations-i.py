class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        d1={}
        d2={}
        for i in range(4):
            if i<2:
                if s1[i]==s2[i] or s1[i]==s2[i+2]:
                    continue
                else:
                    return False
            else:
                if s1[i]==s2[i] or s1[i]==s2[i-2]:
                    continue
                else:
                    return False
        return True
        