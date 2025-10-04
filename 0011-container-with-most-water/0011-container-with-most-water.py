class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i=0
        j=n-1
        max_water=-1000000000000
        while i<j:
            current_water= (j-i)*min(height[i],height[j]);
            if current_water>max_water:
                max_water=current_water
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water







        
        