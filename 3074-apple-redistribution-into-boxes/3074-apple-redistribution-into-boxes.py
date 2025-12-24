class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        sm=sum(apple)
        capacity.sort()
        res=0
        i=len(capacity)-1
        while i>=0:
            res+=1
            sm-=capacity[i]
            i-=1
            if sm<=0:return res
        return res