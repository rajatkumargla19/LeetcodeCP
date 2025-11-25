class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        res=1
        if k%2==0 or k%5==0:return -1
        if k==1:return 1
        length=1
        st=set()
        while True:
            rem=res%k
            if rem==0:
                return length
            if rem not in st:
                st.add(rem)
                res=rem*10+1
                length+=1
            else:
                return -1
        return -1

            
        