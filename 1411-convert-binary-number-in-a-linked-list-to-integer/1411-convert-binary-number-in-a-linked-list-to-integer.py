# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        print(n)
        temp=head
        res=0
        while temp:
            res+=temp.val*2**(n-1)
            n-=1
            temp=temp.next
        return res


        