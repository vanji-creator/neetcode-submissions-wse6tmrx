# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(-1,head)
        left=dummy
        right=dummy
        k=n
        while k>0:
            right=right.next
            k-=1
        
        while right.next:
            right=right.next
            left=left.next

        left.next=left.next.next
        return dummy.next
