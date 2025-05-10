class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # (6,2),  (11,0)=12
        # diff= 5 

        # (4,2) (5,0)=5
        # diff=min_sum1=6....min_sum=5
        n1=len(nums1)
        n2=len(nums2)
        minSum1,minSum2=0,0
        zero1,zero2=0,0
        for i in range(n1):
            if nums1[i]:
                minSum1+=nums1[i]
            else:
                zero1+=1
        for i in range(n2):
            if nums2[i]:minSum2+=nums2[i]
            else:zero2+=1
        # print(minSum1,zero1)
        # print(minSum2,zero2)
        
        minSum1+=zero1
        minSum2+=zero2
        print(minSum1,minSum2)
        # return 12
        if minSum1<minSum2:
            if zero1:return max(minSum1,minSum2)
            else:return -1
        elif minSum1>minSum2:
            if zero2:return max(minSum1,minSum2)
            else:return -1
        else:
            return minSum1



         