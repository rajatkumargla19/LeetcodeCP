class Solution:
    def maximum69Number (self, nums: int) -> int:
        nums=list(str(nums))
        n=len(nums)
        for i in range(n):
            if nums[i]=="6":
                nums[i]="9"
                break
        return int("".join(nums))
                