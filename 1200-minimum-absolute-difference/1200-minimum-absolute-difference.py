class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n=len(arr)
        res=[]
        min_diff=arr[1]-arr[0]
        for i in range(1,n):
            # if not(res):
            #     res.append([arr[i-1],arr[i]])
            # else:
            #     if (arr[i]-arr[i-1])<min_diff:
            #         min_diff=arr[i]-arr[i-1]
            #         res= [arr[i-1],arr[i]] 
            #     elif (arr[i]-arr[i-1])==min_diff:
            #         res.append([arr[i-1],arr[i]])
            if not(res) or (arr[i]-arr[i-1])==min_diff:
                res.append([arr[i-1],arr[i]])
            elif (arr[i]-arr[i-1])<min_diff:
                res= [[arr[i-1],arr[i]]]
                min_diff=arr[i]-arr[i-1]
                

        return res
        