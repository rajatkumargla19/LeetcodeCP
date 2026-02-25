class Solution:
    def count_setBits(self,x):
        count=0
        while x:
            if x%2:count+=1
            x//=2
        return count
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr_by_bit=[[] for i in range(32)]
        n=len(arr)
        for i in range(n):
            arr_by_bit[Solution().count_setBits(arr[i])].append(arr[i])
        # print(arr_by_bit)
        res=[]
        for i in range(32):
            for j in range( len(arr_by_bit[i])  ):
                res.append(arr_by_bit[i][j])
        return res
        


        