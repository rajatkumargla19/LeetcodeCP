class Solution:
    def minOperations(self, s: str) -> int:
        # 01000101...answer 1
        # 000101..1
        # 11(0)100(1)0101....
        # 11(0)11(0)11(0)11(0)1....
        # 10101010*1&...4
        # # 11 11 11 11 1
        s=list(s)
        count=0
        n=len(s)
        # 10010100
        #   10101
        # 111111111
        #  0 0 0 0
        # 0 0 0 0 0
        # 001
        count1=0
        count2=0
        # considering given string is starting from 0
        current='0'
        for i in range(0,n):
            if current!=s[i]:
                current=s[i]
                
            else:
                current='1' if s[i]=='0' else '0'
                count1+=1
        # assuming that given string is starting from 1
        current='1'
        for i in range(0,n):
            if current!=s[i]:
                current=s[i]
            else:
                current='1' if s[i]=='0' else '0'
                count2+=1
        return min(count1,count2)

        print(count1)
        return 2