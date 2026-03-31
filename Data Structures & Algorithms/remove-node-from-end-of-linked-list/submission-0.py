# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # FIX 1: Create a REAL dummy node that points to head
        dummy = ListNode(0, head)
        
        # FIX 2: Start pointers at dummy (position -1)
        left = dummy
        right = dummy
        
        # Standard Sliding Logic (Same as yours, just adapted for dummy)
        # Move right n steps forward
        k = n
        while k > 0:
            right = right.next
            k -= 1
        
        # Move both until right hits the end
        while right.next:
            right = right.next
            left = left.next

        # Delete the node
        left.next = left.next.next
        
        # FIX 3: Return the real start of the list
        return dummy.next