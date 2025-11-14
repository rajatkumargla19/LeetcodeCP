class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat=[[0 for i in range(n+1)] for j in range(n+1)]
        for q in queries:
            for r in range(q[0],q[2]+1): # 0 2
                mat[r][q[1]] +=1
                if (q[2]+1)<(n+1):
                    mat[r][q[3]+1]-=1
        # print(mat) 
        for r in range(n+1):
            for c in range(1,n+1):
                mat[r][c]+=mat[r][c-1]
        # print(mat)
        return [row[:-1] for row in mat[:-1]]

# [1 0 -1 0]
# [1  1 -1 -1]
# [0  1 0 -1]
# [0  0 0 0]


# [1 1 0 0]
# [1 2 1 0]
# [0 1 1 0]
# [0 0 0 0]
            




        


        