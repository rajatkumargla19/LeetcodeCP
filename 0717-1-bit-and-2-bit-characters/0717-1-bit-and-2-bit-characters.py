class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # n=len(bits)
        # if n==1:return True
        # elif n==2:
        #     if bits[-2]==0:return True
        #     return False
        # if bits[-2]==0:return True
        # else:
        #     if bits[-3]==0:return False
        #     else:
        #         if n==3:return True
        #         else:
        #             if bits[-4]==0:return True
        #             return False
        
# [1 0 (1 0 0) ]
# 0 0 0....True
# 1) (1 0...
# if 2nd last digit is 1 then check 3rd last.. if it is also 1 then check 4th last for 1/0 
# if 3 last digit is 0 then return False

# Approach:
#  if 2nd last is 0 ...return True
#  else: 
#       if 3rd last is 0...return False
#       else: 
#         if 4th last is 0..return True
#         else:return False
# else: 
#     return True
        n=len(bits)
        i=0
        while i<n:
            if i==n-1:
                return True
            if bits[i]==1:
                i+=2
            else:
                i+=1
            
        return False


        