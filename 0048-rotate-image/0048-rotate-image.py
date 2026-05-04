class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TRICK: first transpose  => then swap ith column with n-i-1th column
        n=len(arr);
        for i in range(n):
            for j in range(i,n):
                arr[i][j], arr[j][i]=arr[j][i] ,arr[i][j];
        print(arr)
        for i in range(n):
            for j in range(n//2):
                arr[i][j],arr[i][n-1-j]=arr[i][n-1-j],arr[i][j]
        return arr


        

