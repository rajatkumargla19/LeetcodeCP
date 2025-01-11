class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        # Approach: jin characters ki freq even hai, unse maximum 2*count of all  characters with even freqency palindrome strings generate ki jaa sakti hai [minimum 1 string generate ki jaa sakti hai]... understanding this is the main trick here
        # AND jin characters ki freq odd hai unse ,maximum+minimum n palindrome strings generate ki jaa sakti hai, no choice available here for those characters...

        freq=[0]*26
        odds=0
        n=len(s)
        # agar length of given input string hi k se less ho then return False directly
        if n<k:return False
        for i in range(n):
            freq[ord(s[i])-97]+=1
        # counting the characters with odd frequency
        for i in freq:
            if i%2:
                odds+=1
        # print(freq)
        # print(odds)
        # Agar number of characters with odd frequency less than k ho, tab bhi False return kar do 
        if odds>k:return False
        return True
        