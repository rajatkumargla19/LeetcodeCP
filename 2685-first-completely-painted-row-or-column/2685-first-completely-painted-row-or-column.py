class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # Approach: maintain a location dictionery for the fast access of each element present in the given arr. take two external arr those will help us in maintaining the current count of each filled element row-wise and column-wise too.
        # TC=2*O(M*N)
        # SC=O(max(m,n))
        row=len(mat)
        col=len(mat[0])
        locations={}
        for i in range(row):
            for j in range(col):
                locations[mat[i][j]]=[i,j]
        # print(locations)
        row_counter=[0]*row
        col_counter=[0]*col
        for i in range(len(arr)):
            row_counter[locations[arr[i]][0]]+=1
            if row_counter[locations[arr[i]][0]]==col:
                return i
            col_counter[locations[arr[i]][1]]+=1
            if col_counter[locations[arr[i]][1]]==row:
                return i

        
        
        
        
        
        
        
                # [1,4,5,2,6,3]  [[4,3,5],[1,2,6]]
            # row_counter=[,1]
            # col_counter=[,,]


