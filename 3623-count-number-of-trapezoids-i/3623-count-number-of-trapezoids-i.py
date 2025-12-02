class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod=10**9+7
        ans=0
        mp={}
        for i in points:
            # mp[i[1]]+=1
            if i[1] not in mp:
                mp[i[1]]=1
            else:
                mp[i[1]]+=1
        # print(mp)
        # return 10
        edgesSum=0
        for i in mp:
            edges=(mp[i]*(mp[i]-1))//2
            ans=(ans+edges*edgesSum)%mod
            edgesSum+=edges
        return ans


        