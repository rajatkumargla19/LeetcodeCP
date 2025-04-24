class Solution:
    def countLargestGroup(self, n: int) -> int:
    #    9999=36 maximum sum of digits ho sakta hai when n= 10**4 as per the constriant given in the question...
        digit_sum=[0]*37
        maxx=0
        for i in range(1,n+1):
            temp=0
            while i:
                temp+=i%10
                i//=10
            digit_sum[temp]+=1
            maxx=max(maxx,digit_sum[temp])
           
        print(maxx)
        # return 10
        res=0
        for i in range(37):
            if digit_sum[i]==maxx:res+=1
        return res




        