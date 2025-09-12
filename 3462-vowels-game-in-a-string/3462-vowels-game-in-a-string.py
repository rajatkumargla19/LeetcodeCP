class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # vowel cons
        #   3     0  true
        #   2    2   true
        #   2   2    true
        #   2   1    true
        #   0   4    False
        #   4   5    true
            # 10  0    true


        vowels=0
        n=len(s)
        vowel_arr=['a','e','i','o','u'];
        for i in range(n):
            if s[i] in vowel_arr:
                vowels+=1
        return False if vowels==0 else True
        