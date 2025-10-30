class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
      
    #   [inf inf 3 inf inf]
    #   [1 2 3 2 1]  3 operation

    #   [3,inf,inf,2]
    #   [1 1 1 1]
    #   [0,0,0,0,0] res=3

    #   [ 0 0 0 0 0 ] res=7
    # #   [ 0 0 0 0 0 ]

    # # TC...min heap..log2n *n
        n=len(target)
        res=target[0]
        for i in range(n-1):
            if target[i]<target[i+1]:
                res+=target[i+1]-target[i]
        return res