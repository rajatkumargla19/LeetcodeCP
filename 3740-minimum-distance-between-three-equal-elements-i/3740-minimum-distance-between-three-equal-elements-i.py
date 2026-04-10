class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # 1: [0,2,3,5,10]
        n=len(nums)
        freq={}
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]]=[i]
            else:
                freq[nums[i]].append(i)
        # print(abs(3-10))
        # return 5
        res=float('inf')
        for key in freq:
            if len(freq[key])>=3:
                arr=freq[key]
                m=len(arr)
                for i in range(m-2):
                    res=min(res,abs(arr[i]-arr[i+1])+abs(arr[i+1]-arr[i+2])+abs(arr[i+2]-arr[i]))
        return res if res!=float('inf') else -1
        