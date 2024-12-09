class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        [1,2,3,4,1]
        [1,2,1,2]
        n=len(nums)
        parity=[1]
        for i in range(1,n):
            if (nums[i-1]%2)^(nums[i]%2):
                parity.append(parity[-1]+1)
            else:
                parity.append(1)
        print(parity)
        res=[]
        for qr in queries:
            res.append(True if  (parity[qr[1]]-parity[qr[0]])==(qr[1]-qr[0]) else False )
        return res



