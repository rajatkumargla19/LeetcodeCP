class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={}
        ball=[0]*5
        # ablon
        n=len(text)
        for i in range(n):
            if text[i]=="b":ball[0]+=1
            elif text[i]=="a":ball[1]+=1
            elif text[i]=="l":ball[2]+=1
            elif text[i]=="o":ball[3]+=1
            elif text[i]=="n":ball[4]+=1
        print(ball)
        mn1=min(ball[0],ball[1],ball[4])
        mn2=min(ball[2],ball[3])
        return mn1 if mn2>=2*mn1 else mn2//2
        
