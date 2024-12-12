import heapq as hq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # This problem is very simple ,it is just to reduce maintain a max heap  every time we select max element of the complete array
        gifts=[-v for v in gifts]
        hq.heapify(gifts)
        # print(gifts)
        while k:
            # # gifts=math.floor(gifts[0]**0.5)
            # x=gifts.heappop
            # k-=1
            # # How to reduce the time for maintaining _heapify_max() all the time ....
            

            # Another solution 
            
            ele=hq.heappop(gifts)
            ele*=(-1)
            ele=math.floor(ele**(0.5))
            hq.heappush(gifts,-ele);
            # hq._heapify_max(gifts)
            k-=1


        print(gifts)
        return -sum(gifts)