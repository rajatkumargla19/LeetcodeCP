class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # 1000 999999999
        nums.sort()
        map=[[] for i in range(82)]
        n=len(nums)
        for i in range(n):
            summ=0
            temp=nums[i]
            while temp:
                summ+=temp%10
                temp//=10
            map[summ].append(nums[i])
        print(map)
        res=-1
        for i in range(82):
            if len(map[i])>=2:
                res=max(res,map[i][-1]+map[i][-2])
        return res

        
           

        