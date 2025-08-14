class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        i=0
        j=1
        res=""
        max_res=-1
        while j<n:
            if j<n:
                if num[i]==num[j]:
                    if j-i+1==3:
                        if int(num[i:j+1])>max_res:
                            max_res=int(num[i:j+1])
                            res=num[i:j+1]

                    j+=1
                else:
                    i=j
                    j+=1
        return res
            




        