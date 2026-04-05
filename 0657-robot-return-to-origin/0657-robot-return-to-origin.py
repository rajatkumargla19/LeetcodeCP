class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # up/down  +1 -1
        # left/ right +2 -2
        pos1=0
        pos2=0
        i=0
        n=len(moves)
        for i in range(n):
            if moves[i]=="U":pos1+=1
            elif moves[i]=="D":pos1-=1
            elif moves[i]=="L":pos2+=1
            else:pos2-=1
        return True if (not(pos1) and not(pos2))  else False

        