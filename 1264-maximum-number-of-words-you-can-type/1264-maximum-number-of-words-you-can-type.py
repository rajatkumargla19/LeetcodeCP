class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        st=set()
        for w in brokenLetters:
            if w not in st:
                st.add(w)
        sp=list(text.split(" "))
        print(st,sp)
        res=0
        for w in sp:
            flag=True
            for ww in w:
                if ww in st:
                    flag=False
                    break
            if flag==True:
                res+=1
        return res
