class Solution:
    def maxScore(self, s: str) -> int:
        one=0
        n=len(s)
        for i in range(n):
            if s[i]=='1':
                one+=1

        max_score=0
        current_score=0
        zero_so_far=0
        one_so_far=0
        for i in range(n-1):
            if s[i]=='0':
                zero_so_far+=1
            else:
                one_so_far+=1
            current_score=zero_so_far+(one-one_so_far)
            if current_score>max_score:
                max_score=current_score
        return max_score
        