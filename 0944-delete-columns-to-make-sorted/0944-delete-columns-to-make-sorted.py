class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        colm_to_del=0
        for i in range(len(strs[0])):
            flag=False
            for j in range(1,len(strs)):
                if strs[j-1][i]>strs[j][i]:
                    flag=True
                    break
            if flag:
                colm_to_del+=1
        return colm_to_del



        