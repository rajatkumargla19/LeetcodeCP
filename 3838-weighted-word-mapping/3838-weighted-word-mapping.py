class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        # n=len(words)
        for word in words:
            weight=0
            for j in word:
                weight+=weights[ord(j)-97]
            weight%=26
            res=res+chr(97+25-weight )
        return res