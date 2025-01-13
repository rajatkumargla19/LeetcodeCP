class Solution:
    def minimumLength(self, s: str) -> int:
        # Approach: if frequency of a char is even , then it will finally remain 2 only, but if the frequency of the character is odd then only 1 is going to be the remaining... 
        i=0
        temp=[[] for i in range(26)]
        for i in range(len(s)):
            temp[ord(s[i])-97].append(i)
        # print(temp)
        res=0
        for i in range(26):
            res+=(1 if len(temp[i])%2 else 2) if temp[i] else 0
        return res
        

        