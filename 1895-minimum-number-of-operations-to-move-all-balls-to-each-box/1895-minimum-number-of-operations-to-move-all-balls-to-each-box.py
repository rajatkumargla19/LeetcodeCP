class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pos=[]
        n=len(boxes)
        for i in range(n):
            if boxes[i]=='1':
                pos.append(i)
        # print(pos)
        res=[]
        for i in range(n):
            x=0
            for j in range(len(pos)):
               x+=abs(pos[j]-i) 
            res.append(x)
        return res
        