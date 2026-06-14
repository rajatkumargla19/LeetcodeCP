# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,x):
        prev = None
        current = x
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev
 





    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse after middle and then twin sum can be found easily
        slow=head
        fast=head
        mid=None
        while fast:
            slow=slow.next
            fast=fast.next.next
            if fast==None:
                mid=slow
        reversed=Solution().reverse(mid);

        one=head
        two=reversed
        max_sum=0
        # print(two)
        while two:
            if one.val+two.val>max_sum:
                max_sum=one.val+two.val
            one=one.next
            two=two.next
        return max_sum



        