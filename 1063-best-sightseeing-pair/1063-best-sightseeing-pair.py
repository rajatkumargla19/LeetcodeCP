class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        prefix=[values[0]]
        for i in range(1,n):
            prefix.append(max(prefix[-1],values[i]+i))
        print(prefix)
        res=0
        for i in range(1,n):
            res=max(res,prefix[i-1]+values[i]-i)
        return res

        