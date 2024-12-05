class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m=len(str1)
        n=len(str2)
        i=0
        j=0
        while i<m and j<n:
            if str2[j]=='a':
                search_word='z'
            else:
                search_word=chr(ord(str2[j])-1)
                print(search_word)
            while i<m and j<n and (str1[i]!=str2[j] and str1[i]!=search_word):
                i+=1
            else:
                i+=1
                j+=1
                
        if i<=m and j==n:return True
        return False
