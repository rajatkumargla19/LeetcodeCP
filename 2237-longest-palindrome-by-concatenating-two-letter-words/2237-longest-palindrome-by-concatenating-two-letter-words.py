class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # Approach::: 
        self_palin=0
        mp={};
        n=len(words);
        # Initializing the map for counting the frequencies..
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
                
                mp[key]=[]
                mp[key[::-1]]=[]

            elif mp[key] and key==key[::-1]:
                # jab key palindrome ho and uski freq odd ho to us time pe keval 1 me hi add hogi at last me so self_palin is used to track whether the freq of current key is odd or not. If yes then we are adding contribution by reducing 1 from the frequency.... 
                if len(mp[key])%2==1:
                    res+=(len(mp[key])-1)*2
                    self_palin=2
                else:
                    # agar current key palindrome but uski freq even hai then this full key will contrubute in the result, so We have added full frequency *2 to the res..
                    res+=len(mp[key])*2
                mp[key]=[]
            # print(res)
        # Here at last, we are adding the frequency to the result...if multiple key are palindromes so the odd frequency will contribute to the result only once... not more than that.

        return res+self_palin

        return 5
        