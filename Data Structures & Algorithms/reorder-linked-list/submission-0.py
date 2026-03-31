# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        fast,slow=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        slow.next=None

        prev=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt

        first,second=head,prev
        while second:
            nxt1,nxt2=first.next,second.next
            first.next=second
            second.next=nxt1
            first=nxt1
            second=nxt2