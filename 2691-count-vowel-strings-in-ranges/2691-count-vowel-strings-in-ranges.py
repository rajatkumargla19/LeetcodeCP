class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        prefix=[0]*n
        vowels=['a','e','i','o','u']
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i]=prefix[i-1]+1
            else:
                prefix[i]=prefix[i-1]
        print(prefix)
        res=[]
        for i in range(len(queries)):
            res.append( prefix[queries[i][1]] - (prefix[queries[i][0]-1] if queries[i][0]>0 else 0 ))
        return res
        