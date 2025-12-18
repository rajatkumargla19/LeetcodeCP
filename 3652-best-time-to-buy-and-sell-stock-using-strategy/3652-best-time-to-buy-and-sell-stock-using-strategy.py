class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # # Approach: it is not DP actually, it is something diffrent 
        # there are two prefix sums are required...
        pre_arr=[prices[0]]
        pre_stocks=[prices[0]*strategy[0]]
        n=len(prices)
        for i in range(1,n):
            pre_arr.append( pre_arr[i-1]+prices[i] )
            pre_stocks.append( pre_stocks[i-1]+prices[i]*strategy[i] )
        # print(pre_arr)
        # print(pre_stocks)
        res=float('-inf')
        for i in range(n-k+1):
            temp=(pre_stocks[i-1] if i-1>=0 else 0)+((pre_stocks[-1]-pre_stocks[i+k-1]) if (i+k-1<(n-1)) else 0    )
            temp2=(pre_arr[i+k-1]-(pre_arr[i-1] if (i-1>=0) else 0) )-(pre_arr[i+(k-1)//2]-(pre_arr[i-1] if (i-1>=0) else 0))
            # print(temp,temp2)
            res=max(res,temp+temp2)
        return max(res,pre_stocks[-1])

        