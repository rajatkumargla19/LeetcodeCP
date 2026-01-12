class Solution:
    def residuePrefixes(self, s: str) -> int:
        n=len(s)
        st=set(s[0])
        res=0;
        for i in range(1,n):
            if len(st)==(i%3):
                res+=1
            st.add(s[i])
        if len(st)==(n%3):
            res+=1
        return res
