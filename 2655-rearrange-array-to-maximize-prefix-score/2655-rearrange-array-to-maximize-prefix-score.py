class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n=len(nums)
        positive=[]
        negative=[]
        zeros=0
        for i in range(n):
            if nums[i]==0:
                zeros+=1
            elif nums[i]>0:
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        if zeros:
            positive.extend([0]*zeros)
        print(positive)
        negative.sort()
        print(negative)
        for i in range(len(negative)-1,-1,-1):
            positive.append(negative[i])
        print(positive)
        res=0
        prefix_sum=0
        for i in range(n):
            prefix_sum+=positive[i]
            if prefix_sum>0:
                res+=1
        return res

        

