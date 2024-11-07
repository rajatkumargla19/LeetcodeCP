class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
    #    [[4],[4,0],[6,2,1,0],[1,2,3,4,5],[2,3],[3,4],[1,2,3]]...
    #    d={4:4,}
    #    1000 1000 10
    #    10+10+4=24
    #    [2,3,4,4,4,1,,,,,,,,,,,,,,,,,,]
    #    [0,0,0,2]
    # Program my logic: We have to find the largest subsequence whose AND is not zero, so what we will do here is: "jin jin numbers me koi bhi set bit common hai, un sabka AND hamesa non-zero hi aayega. so hame number count karne hai jinme same set bit present hai"
    # setbits_position= #    [[4],[4,0],[6,2,1,0],[1,2,3,4,5],[2,3],[3,4],[1,2,3]]...
    # 4th and 3rd bit 4 number me set hai so all those number if ANDed will generate non-zero number  # so answer will be 4.... very easy intuition...
        bits=[0]*24
        n=len(candidates)
        res=0
        for i in range(n):
            temp=candidates[i]
            bit=0
            while temp:
                bits[bit]+=temp%2
                temp//=2
                res=max(res,bits[bit])
                bit+=1

        # print(bits)
        # res=0
        # for i in range(24):
        #     res=max(res,bits[i])
        return res
