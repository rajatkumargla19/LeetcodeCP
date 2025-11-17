class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index_of_one=None
        for i in range(len(nums)):
            if nums[i]==1:
                if index_of_one==None:
                    index_of_one=i
                else: 
                    if i-index_of_one<=k:
                        return False
                    else:
                        index_of_one=i
        return True

        