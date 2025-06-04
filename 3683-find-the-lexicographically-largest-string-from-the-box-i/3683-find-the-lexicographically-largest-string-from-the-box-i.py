class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n=len(word)
        if numFriends==1:return word
        maxLength=n-numFriends+1
        res=''
        for i in range(n):
            # if i+maxLength>n:
            #     res=max(res,word[i:])
            # else:
            #     res=max(res,word[i:i+maxLength])
            res=max(res,word[i:]) if i+maxLength>n else max(res,word[i:i+maxLength])
        return res
        