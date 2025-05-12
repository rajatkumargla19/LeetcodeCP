class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
    #   [1,3,5] [0,4]
    #   [130,]
        res=[]
        maps={}
        for i in range(len(digits)):
            if digits[i] not in maps:
                maps[digits[i]]=1
            else:
                maps[digits[i]]+=1
        print(maps)
        for i in range(100,999,2):
            visited=[0 for i in range(10)]
            st=str(i)
            visited[int(st[0])]+=1
            visited[int(st[1])]+=1
            visited[int(st[2])]+=1
            flag=1
            for j in range(10):
                if  visited[j] and (j not in maps or maps[j]<visited[j]) :
                    flag=0
                    break
            if flag:
                res.append(i)
        return res
                    
        print(res)
        return res
            
        