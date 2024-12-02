class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # This question is just based on a silly observation....'any number of times' phrase in the first line of the question is very important to be considered...
        res=0
        n=len(matrix)
        count=0
        mini=float('inf')
        for i in range(n):
            for j in range(n):
                res+=abs(matrix[i][j])
                count=count^(matrix[i][j]<0)
                # if matrix[i][j]<0:count+=1
                mini=min(mini,abs(matrix[i][j]))
        if count:
            print(mini)
            return res-2*mini
        return res