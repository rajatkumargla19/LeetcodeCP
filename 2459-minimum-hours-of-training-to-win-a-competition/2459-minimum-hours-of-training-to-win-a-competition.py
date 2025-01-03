class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # energy calculation and experience calculations ko seperately karo... to get the required results...
        # 4+2+
        # 2+
        res=0
        n=len(energy)
        for i in range(n):
            if initialEnergy>energy[i]:
                initialEnergy-=energy[i]
            else:
                res+=(energy[i]-initialEnergy)+1
                initialEnergy+=(energy[i]-initialEnergy)+1
                
                initialEnergy-=energy[i]
        print(res)
        for i in range(n):
            if initialExperience>experience[i]:
                initialExperience+=experience[i]
            else:
                res+=(experience[i]-initialExperience)+1
                initialExperience+=(experience[i]-initialExperience)+1
                
                initialExperience+=experience[i]
        return res
            




        