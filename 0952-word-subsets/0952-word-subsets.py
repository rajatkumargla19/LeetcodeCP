class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        freq1=[0]*26
        n=len(words2)
        for i in range(n):
            freq2=[0]*26
            for j in range(len(words2[i])):
                freq2[ord(words2[i][j])-97]+=1
            for c in range(26):
                freq1[c]=max(freq1[c],freq2[c])
        # print(freq1)
        res=[]
        for i in range(len(words1)):
            freq=[0]*26
            for j in range(len(words1[i])):
                freq[ord(words1[i][j])-97]+=1
            flag=True
            # print(freq)
            for c in range(26):
                if freq1[c] and freq[c]<freq1[c]:
                    # print(words1[i])
                    flag=False
                    break
            if flag:
                res.append(words1[i])
        return res


        