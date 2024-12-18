class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        stack=[0]
        for i in range(1,n):
            if prices[i]>prices[stack[-1]]:
                stack.append(i)
            else:
                while len(stack)>0 and prices[i]<=prices[stack[-1]]:
                    prices[stack[-1]]-=prices[i]
                    stack.pop()
                stack.append(i)
        return prices
            