class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d={}
        n=len(arr)
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]]=[i]
            elif arr[i]==0:
                d[arr[i]].append(i)
                
        print(d)
        for i in range(n):
            if 2*arr[i] in d and arr[i]!=0:
                return True
            elif arr[i]==0 and len(d[arr[i]])>1:
                return True
        return False