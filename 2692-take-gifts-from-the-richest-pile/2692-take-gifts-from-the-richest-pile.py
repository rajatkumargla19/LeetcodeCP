import heapq as hq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # This problem is very simple ,it is just to reduce maintain a max heap  every time we select max element of the complete array

        hq._heapify_max(gifts)
        # print(gifts)
        while k:
            gifts[0]=math.floor(gifts[0]**0.5)
            k-=1
            # How to reduce the time for maintaining _heapify_max() all the time ....
            hq._heapify_max(gifts)
        print(gifts)
        return sum(gifts)