class Solution:
    def compressedString(self, word: str) -> str:
        res=[]
        i=0
        n=len(word)
        while i<n:
            count=1
            while i+1<n and word[i]==word[i+1]:
                count+=1
                i+=1
                if count==9:break
            res.append(str(count)+word[i])
            i+=1
        return "".join(res)
        