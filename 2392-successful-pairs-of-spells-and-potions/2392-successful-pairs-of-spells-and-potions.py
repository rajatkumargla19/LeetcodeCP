class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ' Approach:: sort potion and find found=ceil(success/spells[i]) for each array element. find element greater than or equal to the found using binary search...'
        #  udayveer sukhpal 
        potions.sort()
        result=[]
        sp=len(spells)
        po=len(potions)
        for i in range(sp):
            found=ceil(success/spells[i])
            lo=0
            hi=po-1
            flag=0
            while lo<=hi:
                mid=(lo+hi)//2
                if potions[mid]>=found:
                    if (mid==0 or potions[mid-1]<found):
                        result.append(po-mid)
                        flag=1
                        break
                    else:
                        hi=mid-1
                elif potions[mid]<found:
                    lo=mid+1
                
            if flag==0:
                if mid==0:
                    result.append(po-1-mid)
                else:
                    result.append(0)
                
        return result























        # # [5,1,3]  [1 2 3 4 5]
        # potions.sort()
        # s=len(spells)
        # p=len(potions)
        # res=[]
        # for i in range(s):
        #     # mid=m//2
        #     lo=0
        #     hi=p-1
        #     while lo<=hi:
        #         mid=(lo+hi)//2
        #         # if potions[mid]*spells[i]<success:
        #         #     if mid==0 or mid==n-1:
        #         #         break
        #         #     elif potions[i]*spells[mid+1]>=success:
        #         #         break
        #         #     elif potions[i]*spells[mid+1]<
                    
        #         if spells[i]*potions[mid]>=success:
        #             if mid==0:

        #             hi=mid-1
        #         else:
        #             lo=mid+1
        #     if hi==-1:
        #         res.append(p)
        #     elif lo==p:
        #         res.append(0)
        #     else:
        #         res.append(p-mid)
        # return res
        # # [1lh,2,3,4,5,6,8]


                