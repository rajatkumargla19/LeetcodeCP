# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if head.next==None:
            # head=None
            # return head
            return None
        n=0
        while temp!=None:
            n+=1
            temp=temp.next
        temp=head
        # print(n)
        middle=n//2
        while middle>0 :
            prev=temp
            temp=temp.next
            middle-=1
        if temp.next!=None:
            nexx=temp.next
        else:
            nexx=None
        
        # print(prev.val)
        # print(temp.val)
        # print(nexx) 
        # temp.val, nexx.val)
        prev.next=nexx
        temp.next=None
        return head
        




        