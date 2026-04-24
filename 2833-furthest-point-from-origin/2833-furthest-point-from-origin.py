class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        # 1+0-1+1+0+0-1=
        # dash_count=3
        # moves=1
        # dash_count=1+1+1+1
        n=len(moves)
        dashes=0
        steps=0
        for i in range(n):
            if moves[i]=="_":dashes+=1
            elif moves[i]=="L":
                steps+=1
            else:steps-=1
        return abs(steps)+dashes