class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Approach::: 
        self_palin=False
        mp={};
        n=len(words);
        for i in range(n): 
            if words[i] not in mp:
                mp[words[i]]=[i]
            else:
                mp[words[i]].append(i)
        print(mp)
        res=0
        for key in mp:
            if mp[key] and key[::-1] in mp and key!=key[::-1]:
                res+=min(len(mp[key]),len(mp[key[::-1]]))*4
                # res+= abab baba
                mp[key]=[]
                mp[key[::-1]]=[]

            elif mp[key] and key==key[::-1]:
                
                if len(mp[key])%2==1:
                    res+=(len(mp[key])-1)*2
                    self_palin=True
                else:
                    res+=len(mp[key])*2
                mp[key]=[]
            print(res)
        # print(self_palin)
        if self_palin:
            res+=2
        return res

        return 5
        