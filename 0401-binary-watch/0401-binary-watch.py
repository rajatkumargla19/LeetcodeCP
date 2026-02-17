class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn>8:return []
        res=[]
        for hh in range(12):
            for mm in range(60):
                if bin(hh).count("1")+bin(mm).count("1")==turnedOn:
                    hour=str(hh)
                    minute=("0" if mm<10 else "")+str(mm)
                    res.append(hour+":"+minute)
        
        return res


        