class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        positives=0
        n=len(nums)
        temp=[]
        for i in range(n):
            if nums[i]>=0:
                positives+=1
                temp.append(nums[i])
        k=k%positives if positives else k
        
        temp=temp[k:]+temp[:k]
        j=0
        # print(k,temp)
        for i in range(n):
            if nums[i]>=0:
                # print(temp[j])
                nums[i]=temp[j]
                j+=1
        return nums




        