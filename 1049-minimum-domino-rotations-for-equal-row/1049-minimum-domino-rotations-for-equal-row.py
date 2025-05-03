class Solution:
    def checking(self,arr,bottoms):
        map1={}
        m=len(arr)
        max_count=1
        max_ele=arr[0]
        for i in range(m):
            if arr[i] not in map1:
                map1[arr[i]]=1
            else:
                map1[arr[i]]+=1
                if max_count<map1[arr[i]]:
                    max_count=max(max_count,map1[arr[i]])
                    max_ele=arr[i]
        rotations1=0
        for i in range(m):
            if arr[i]!=max_ele:
                if bottoms[i]!=max_ele:
                    return float('inf')
                else:
                    rotations1+=1
        return rotations1
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res=min(self.checking(tops,bottoms),self.checking(bottoms,tops))
        return res if res!=float('inf') else -1


        