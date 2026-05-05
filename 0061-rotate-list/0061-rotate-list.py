# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n=0
        temp=head
        while temp!=None:
            n+=1
            temp=temp.next
        if n>0:
            k=k%n
        if head==None or head.next==None or k==0:
            return head
        temp=head
        # k=k%n
        k=n-k
        while temp!=None and k>1:
            temp=temp.next
            k-=1
        print(temp)
        removed=temp.next
        temp.next=None
        temp2=removed
        if removed==None:
            return 
        while temp2.next!=None:
            temp2=temp2.next
        temp2.next=head
        return removed
        