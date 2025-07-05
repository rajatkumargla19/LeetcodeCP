class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        n=len(arr)
        for i in range(n):
            if arr[i] not in freq:
                freq[arr[i]]=1
            else:
                freq[arr[i]]+=1
        res=-1
        for i in freq:
            if i==freq[i]:
                res=max(res,i)
        return res
        