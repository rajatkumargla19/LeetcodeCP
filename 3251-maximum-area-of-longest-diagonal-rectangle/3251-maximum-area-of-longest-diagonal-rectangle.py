class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        n=len(dimensions) 
        max_diagonal=0 ;
        max_area=0 ;
        for i in range(n): 
            diag= ( (dimensions[i][0]**2) + (dimensions[i][1]**2) ) **(0.5)
            area= dimensions[i][0] * dimensions[i][1]
            # print(diag,area)
            if diag> max_diagonal:
                max_diagonal=diag
                max_area=area
            elif diag==max_diagonal:
                if area>max_area:
                    max_area=area
        return max_area
                

        