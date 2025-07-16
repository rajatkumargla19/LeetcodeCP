class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odds_seq=0
        # even_seq_len=0
        diffparity_seq=1
        n=len(nums)
        
        for i in range(n):
            if nums[i]%2:
                odds_seq+=1
            if i!=0:
                if nums[i]%2!=nums[i-1]%2:
                    diffparity_seq+=1
        return max(odds_seq,n-odds_seq,diffparity_seq)

            


        