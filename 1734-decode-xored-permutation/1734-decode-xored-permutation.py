class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n=len(encoded)+1
        perm_xor=0
        for i in range(1,n+1):
            perm_xor^=i
        enc_xor=0
        for i in range(1,n-1,2):
            enc_xor^=encoded[i]
        a0=perm_xor^enc_xor;
        ans=[a0]
        for i in range(1,n):
            print(ans[-1])
            print(encoded[i-1])
            ans.append(ans[i-1]^encoded[i-1])
            
        return ans


        