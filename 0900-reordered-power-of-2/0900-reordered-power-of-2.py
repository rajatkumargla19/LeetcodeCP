class Solution:
    def reorder(self,n):
        freq=[0]*10
        while n>0:
            freq[n%10]+=1
            n//=10
        return freq
    def reorderedPowerOf2(self, n: int) -> bool:
        freq=Solution().reorder(n)
        for i in range(0,30):
            if freq==Solution().reorder(1<<i):
                return True
        return False
