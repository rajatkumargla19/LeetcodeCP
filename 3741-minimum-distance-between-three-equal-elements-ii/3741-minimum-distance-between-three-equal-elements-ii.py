class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # {1:[0,1,3]}
        n=len(nums)
        freq={}
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]]=[i]
            else:
                freq[nums[i]].append(i)
        
        # print(freq)
        # return 5
        res=float('inf')
        for key in freq:
            ll=len(freq[key])
            arr=freq[key]
            if ll>=3:
                for i in range(ll-2):
                    res=min(res,abs(arr[i]-arr[i+1])+abs(arr[i+1]-arr[i+2])+abs(arr[i+2]-arr[i]) )
        return res if res!=float('inf') else -1


        