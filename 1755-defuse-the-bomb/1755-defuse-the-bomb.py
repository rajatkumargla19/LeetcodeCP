class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # prefix_sum and suffix_sum
        n=len(code) 
        prefix_sum=[0]*n
        # suffix_sum=[0]*n

        res=[0]*n
        if k==0:
            return [0]*n
        elif k>0:
            prefix_sum[0]=code[0]
            for i in range(1,n):
                prefix_sum[i]=prefix_sum[i-1]+code[i]    
        elif k<0:  
            prefix_sum[0]=code[-1]
            for i in range(n-2,-1,-1):
                prefix_sum[n-i-1]=prefix_sum[n-i-2]+code[i]
            print(prefix_sum)
        for i in range(n):
                if i+abs(k)<n: 
                    res[i]=prefix_sum[i+abs(k)]-prefix_sum[i]
                else:
                    res[i]=prefix_sum[-1]+prefix_sum[(i+abs(k))%n]-prefix_sum[i]
        return res if k>0 else res[::-1]

