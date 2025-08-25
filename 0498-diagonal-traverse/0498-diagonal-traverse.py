class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 0 1 2 3 4
        # 1 5 6 7 8
        # 2 9 1 2 3
        # 3 1 2 3 4
        # 4 1 2 3 4
        # 5 1 2 3 4
        # Approach: 1: while going down, there may be two boundaries those are..either left boundary or bottom boundary... If left boundary aaye, move down once | if bottom boundary aaye, move right once | if both left+ bottom dono boundary aaye, end the process
        # 2: while going up, there also may be two boundaries,those are... either top or right boundary...
        # If right ya (right+top) boundary aaye, move down once | If top boundary aaye, move right once...
        m=len(mat)
        n=len(mat[0])
        res=[]
        move=True # true means up
        i,j=0,0
        while i<m and j<n:
            if move:
                res.append(mat[i][j])
                while i>0 and j<n-1:
                    i-=1
                    j+=1
                    res.append(mat[i][j])
                else:
                    if j==n-1:
                        # if i<m:i+=1
                        i+=1
                    else:
                        j+=1
                    move=not(move)
            else:
                res.append(mat[i][j])
                while i<m-1 and j>0:
                    j-=1
                    i+=1
                    res.append(mat[i][j])
                else:
                    if i==m-1:
                        j+=1
                    else:
                        i+=1
                    move=not(move)
        return res

# res=[1,2,4,7,5,3,6,8,9]



            
           




