import math
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        # approach: right se first zero ke baad wale 1 ko invert karlo...agar
        # rightmost zero ke baad koi 1 na ho to consider the number to be -1 
        ans=[]
        for i in range(len(nums)):
            digit=int(math.log2(nums[i])+1)
            #print(digit)
            power=0
            flag=False
            while power<=digit:
                if ((1<<(power)) & nums[i])==0:
                    if power==0:ans.append(-1)
                    else:ans.append(nums[i]^(1<<(power-1)) )
                    # flag=True
                    break
                power+=1
            # if not(flag):
            #     ans.append(-1) 
        return ans 