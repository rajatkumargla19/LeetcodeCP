class Solution:
    def isValid(self, word: str) -> bool:
        vowel=['a','e','i','o','u','A','E','I','O','U']
        digits=['0','1','2','3','4','5','6','7','8','9']
        n=len(word)
        if n<3:return False
        vowel_flag=False
        cons_flag=False
        for i in range(n):
            asci=ord(word[i])
            if (asci>=65 and asci<=90) or (asci>=97 and asci<=122) or (asci>=48 and asci<=57):
                if word[i] in vowel:
                    vowel_flag=True
                elif word[i] not in digits:
                    cons_flag=True
            else:
                return False
        if vowel_flag and cons_flag:return True
        return False


        