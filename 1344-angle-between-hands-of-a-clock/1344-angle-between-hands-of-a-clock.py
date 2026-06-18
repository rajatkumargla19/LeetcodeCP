class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 12:03
        # 1 minute me hour wali needle kitni degree chalti hai 
        # 360....30...
        # minute wali ke 1 degree ghumne pe hours wali 1/12 degrre ghumti hai 
        # approach: sabse pahle given minutes ko degree me convert karlo *6 karke
        # 3:15
        # 3*30+90/12: 90 degree
        # 90+7.5-90
        minute_degree=minutes*6
        hour_degree=(hour*30)%360+minute_degree/12
        print(minute_degree,hour_degree)
        return min(  abs(hour_degree-minute_degree), (360-hour_degree+minute_degree), (360-minute_degree+hour_degree) )
        