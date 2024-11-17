class Solution:
    def resultsArray(self, arr: List[int], k: int) -> List[int]:
        if k==1:return arr
        res=[]
        flag=-1 
        n=len(arr)
        maxx=arr[0]
        for i in range(1,k):
            if arr[i-1]>=arr[i] or (arr[i-1]+1)!=arr[i]:
                flag=i
            if flag!=-1:
                maxx=arr[i]
            else:
                maxx=max(maxx,arr[i])
        #   [3,2,43,44,45]
        if flag==-1:
            res.append(maxx)
        else:
            res.append(-1)
        for i in range(k,n): #1<=2-2+1
            if arr[i-1]>=arr[i] or ((arr[i-1]+1)!=arr[i]):
                flag=i
                maxx=arr[i]
                res.append(-1)
            elif flag==-1 or (flag<=(i-k+1)):
                maxx=max(maxx,arr[i])
                res.append(maxx)
            else:
                res.append(-1)
            

        # print(maxx)
        return res    
            
            


        
        