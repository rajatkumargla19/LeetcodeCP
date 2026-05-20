class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Approach: maintain a freq map. when we get frequency of an element to 2, then immediately increase the commoN_count by 1 as this element has occured in both arrays now and is common in both the arrays.... and update the same in the both res arr.
        


        n=len(A)
        res=[0]*n
        res[n-1]=n
        # [5 1 4 3 2]
        # [1 5 2 3 4]
        # [0,2,2,3,5]
        # d1={}
        # res=[0, ]
        # 10111000000000000000
        # freq={5:2,1:2,4:1,2:2,3:2}
        # common_count=2
        # res=[0,2,2,3,0]
        freq={}
        common_count=0
        for i in range(n):
            if A[i] not in freq:
                freq[A[i]]=1
            else:
                freq[A[i]]=2
                common_count+=1
            if B[i] not in freq:
                freq[B[i]]=1
            else:
                freq[B[i]]=2
                common_count+=1
            res[i]=common_count
        return res
