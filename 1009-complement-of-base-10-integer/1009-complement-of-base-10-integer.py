class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if not(n) else n^((1<<n.bit_length())-1) 

        # return ~n
        # 101

        # 010

        