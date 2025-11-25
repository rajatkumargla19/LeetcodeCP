class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        res=1
        # Agar k even hai ya multiple of 5 hai then no number ending with 1 can be a multiple of k , so return just -1
        if k%2==0 or k%5==0:return -1
        # when k==1 then return n=1 directly
        if k==1:return 1
        length=1
        # to check whether remainder has not started repeating itself.. if it happens then we are directly going to return -1... as repetition of remainder wont give us the desired result
        st=set()
        while True:
            rem=res%k
            if rem==0:
                return length
            if rem not in st:
                st.add(rem)
                # we have to generate the new number from remainder itself while maintaing the current length of the number...below line is the crux of this question
                res=rem*10+1
                length+=1
            else:
                return -1
        # return -1

            
        