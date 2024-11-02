class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sent=sentence.split(" ")
        n=len(sent)
        for i in range(n-1):
            if i==0:
                if sent[i][-1]!=sent[i+1][0]:return False
            else:
                if sent[i][-1]!=sent[i+1][0]:return False
        if sent[0][0]!=sent[-1][-1]:return False
        return True


            
        