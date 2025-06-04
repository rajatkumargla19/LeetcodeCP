class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        
        if numFriends==1:return word
        max_char='a'
        indices=[]
        n=len(word)
        for i in range(n):
            if word[i]>max_char:
                max_char=word[i]
                indices=[i]
            elif word[i]==max_char:
                indices.append(i)
        # print(max_char)
        # print(indices)
        res=''
        for i in range(len(indices)):
            temp=None
            numF=numFriends
            if indices[i]+1>=numF:
                res=max(res,word[indices[i]:])
            else:
                numF-=indices[i]
                # temp=word[indices[i]:n-numF+1]
                res=max(res,word[indices[i]:n-numF+1])
                # [3:8] abc(defgh)ij
            # print(temp)
            # res=max(res,temp)
        return res





        



        