class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # kab diff even aayega: jab dono partitions ka sum ya to even ho ya dono ka odd ho...
        # 5
        # [(1 2 2]
        # 20
        # [(2 4 6) 8]
        sm=sum(nums)
        n=len(nums)
        res=0
        current_sum=0
        for i in range(n-1):
            current_sum+=nums[i]
            if abs((sm-current_sum)-(current_sum))%2==0:
                res+=1
        return res

        