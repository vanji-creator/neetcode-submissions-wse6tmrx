# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head

        dummyNode=ListNode(-1,head)
        prev=dummyNode

        for _ in range(left-1):
            prev=prev.next

        curr=prev.next

        for _ in range(right-left):
            nxt=curr.next
            curr.next=nxt.next
            nxt.next=prev.next
            prev.next=nxt
        return dummyNode.next