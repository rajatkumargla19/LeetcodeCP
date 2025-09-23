class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=version1.split(".")
        version2=version2.split(".")
        # print(version1)
        # print(version2)
        # return 0
        for i in range(len(version1)):
            version1[i]=int(version1[i])
        
        for i in range(len(version2)):
            version2[i]=int(version2[i])
        print(version1)
        print(version2)
        # return 1
        i=0
        j=0
        while i<len(version1) and j<len(version2):
            if version1[i]>version2[j]:
                return 1
            elif version1[i]<version2[j]:
                return -1
            else:
                i+=1
                j+=1
        if i==len(version1) and j==len(version2):return 0
        while i<len(version1):
            if version1[i]>0:
                return 1
            i+=1
        # print('working')
        while j<len(version2):
            if version2[j]>0:
                return -1
            j+=1
        return 0

        
        