class Solution:
    def count_setBits(self,x):
        setBits=0
        while x:
            if x%2:setBits+=1
            x//=2
        return setBits
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr_bitwise=[[] for i in range(32)]
        n=len(arr)
        for i in range(n):
            arr_bitwise[Solution().count_setBits(arr[i])].append(arr[i])
        res=[]
        for i in range(32):
            for j in range( len(arr_bitwise[i])  ):
                res.append(arr_bitwise[i][j])
        return res
        


        