class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        st=set()
        n=len(s)
        st_length=0
        factor=1<<k
        for i in range(n-k+1):
            if s[i:i+k] not in st:
                st.add(s[i:i+k])
                st_length+=1
            if st_length==factor:return True
        return st_length==factor
        
            


        