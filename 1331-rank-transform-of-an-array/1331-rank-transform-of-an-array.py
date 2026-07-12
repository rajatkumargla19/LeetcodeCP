class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        temp=[] 
        n=len(arr)
        for i in range(n):
            temp.append(arr[i])
        temp.sort()
        d={}
        rank=1
        for i in range(n):
            if temp[i] not in d:
                d[temp[i]]=rank
                rank+=1                
        # print(d)
        res=[]
        for i in range(n):
            res.append(d[arr[i]])
        # print(res)
        return res
      