class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Approach: kuch ni karna, jis substring me bhi 'D' aaye usko hi +1 karke reverse kar lo  aur 
        # kaam ho jaayega 
        n=len(pattern)
        # 123[45][6789]
        res=[str(i+1) for i in range(n+1)]
        # print(res)
        i,j=0,0
        # 2 pointer approach just to track the length of substring having only 'D'
        while j<n:
            if pattern[j]=='D':
                j+=1
            else:
                if i<j:
                    # print(i,j) used for debugging purposes only
                    res[i:j+1]=res[i:j+1][::-1]
                i,j=j+1,j+1
        # when last substring me only D ho to j ka counter loop se bahar ho jaayega and that case needs to be checked externally 
        if i<j:
            # print(i,j)
            # print(res[i:j+1])
            res[i:j+1]=res[i:j+1][::-1]
        return "".join(res)




        