class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Approach: last index maintain karo... then curr_space ko stretch karte chalo 
        # agar possible ho sake to ...

        n=len(s)
        lastIndex={}
        for i in range(n):
            lastIndex[s[i]]=i
        # print(lastIndex)
        i=0
        res=[]
        while i<n:
            curr_space=[i,lastIndex[s[i]] ]
            print(curr_space)
            i+=1
            while i<=curr_space[1]:
                if lastIndex[s[i]]>curr_space[1]:
                    curr_space[1]=lastIndex[s[i]]
                
                i+=1
            res.append(curr_space[1]-curr_space[0]+1)    
        return res
        