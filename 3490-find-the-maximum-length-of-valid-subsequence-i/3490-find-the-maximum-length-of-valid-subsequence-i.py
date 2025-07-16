class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_seq_len=0
        even_seq_len=0
        diff_parity_seq=1
        n=len(nums)
        
        for i in range(n):
            if nums[i]%2:
                odd_seq_len+=1
            if i!=0:
                if nums[i]%2!=nums[i-1]%2:
                    diff_parity_seq+=1
        return max(odd_seq_len,n-odd_seq_len,diff_parity_seq)
        
            


        