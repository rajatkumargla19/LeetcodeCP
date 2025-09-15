class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact_match=set()
        n=len(wordlist)
        case_match={}
        vowel_match={}
        for i in range(n):
            # code for exact match
            exact_match.add(wordlist[i])
            # code for case mismatch
            word=""
            word2=""
            vowels=['a','e','i','o','u','A','E','I','O','U'];
            for j in wordlist[i]:
                word+=( chr(ord(j)+32) if (65<=ord(j)<=90) else j)
                word2+=((chr(ord(j)+32) if (65<=ord(j)<=90) else j) if (j not in vowels) else '*')
            if word not in case_match:
                case_match[word]=wordlist[i]
            if word2 not in vowel_match:
                vowel_match[word2]=wordlist[i]
        print(exact_match,case_match,vowel_match)
        res=[]
        found=False
        for q in queries:
            if q in exact_match:
                res.append(q)
                continue
            lower="".join([ ( chr(ord(j)+32) if (65<=ord(j)<=90) else j) for j in q] );
            print(lower);
            if lower in case_match:
                res.append(case_match[lower])
                continue
            voweler="".join([("*" if (j in vowels) else (chr(ord(j)+32) if (65<=ord(j)<=90) else j) ) for j in q ] )
            if voweler in vowel_match:
                res.append(vowel_match[voweler])
                continue
            res.append("")
        return res



        

        
        