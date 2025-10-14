class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        i=0
        n=len(nums)
        while (i+2*k-1)<n:
            flag=True
            print(i)
            for j in range(i,i+k-1):
                if nums[j]>=nums[j+1]:
                    flag=False
                    print("working1",i)
                    break
            if flag:
                for j in range(i+k,i+2*k-1):
                    if nums[j]>=nums[j+1]:
                        flag=False
                        print("working",i)
                        break
            print(flag)
            if flag:
                return True
            i+=1
        return False

        


    

