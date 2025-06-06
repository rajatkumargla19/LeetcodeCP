class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res=1
        n=len(arr)
        if n==1:return 1
        greater=False
        i=0
        j=0
        while i<n and j+1<n:
            if arr[j]>arr[j+1]:
                if greater:
                    res=max(res,j-i+1)
                    i=j
                    # j=i

                greater=True
                j+=1
            elif arr[j]<arr[j+1]:
                if not(greater):
                    res=max(res,j-i+1)
                    i=j
                    
                greater=False
                j+=1
            
            else:
                res=max(res,j-i+1)
                # i=j+1
                j+=1
                i=j
                greater=False
                # j=i    # [9,4,2,10,7,8,8i,1,9j]

        return max(res,j+1-i)

                

        