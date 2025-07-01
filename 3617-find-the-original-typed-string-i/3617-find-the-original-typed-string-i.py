class Solution:
    def possibleStringCount(self, word: str) -> int:
        # return 8
        i=0
        j=1
        n=len(word)
        res=1
        if n==1:return 1
        while j<n:
            while j<n and word[i]==word[j]:
                j+=1
            res+=(j-i-1)
            i=j
            j+=1
        return res


        