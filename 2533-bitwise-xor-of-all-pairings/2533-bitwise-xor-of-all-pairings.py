class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Approach: 
        # (1) If nums1 has even number of elements[n1] and array2 has odd number of elements[n2], then in the calculation the result, each element of nums2 will be XORed n1 times and as n1 is already odd so resultant XOR of all of them will not be zero. and it will be equivalent to XOR of all elements of nums2 single time....
        # in the same way all other observation for the calculation of resultant XOR can be done.....
        # this question contains only simple observation related to XOR bitwise operator   
        n1,n2=len(nums1),len(nums2)
        res=0
        if n1%2==0 and n2%2==0:
            return 0
        elif n1%2==1 and n2%2==0:
            for i in range(n2):
                res^=nums2[i]
        elif n1%2==0 and n2%2==1:
            for i in range(n1):
                res^=nums1[i]
        else:
            for i in range(n1):
                res^=nums1[i]
            for i in range(n2):
                res^=nums2[i]
        return res

