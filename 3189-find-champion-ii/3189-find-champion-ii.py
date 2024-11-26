class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # 15 width, 30 feet length 
        # window should be double pataam and mixed with steel (only due to you)
        # lobby should be 4 feet long and 4 feet more in width 
        # 30*21.5=645.... 
        # {1:[2,3],0:[2]}
        # {0:[1],1:[2]}
        d={}
        # n=len(edges)
        for i in range(len(edges)):
            if edges[i][0] not in d:
                d[edges[i][0]]=[edges[i][1]]
            else:
                d[edges[i][0]].append(edges[i][1])
        # print(d)
        temp=[]
        for i in d:
            temp.extend(d[i])
        
        temp=set(temp)
        # print(len(temp))
        if len(temp)<n-1:return -1
        for i in range(n):
            if i not in temp:return i
        

