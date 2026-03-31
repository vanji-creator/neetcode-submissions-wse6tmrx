# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        grp_prev=dummy

        while True:
            kth=self.getKth(grp_prev,k)
            if not kth:
                break
            
            curr=grp_prev.next
            for _ in range(k-1):
                nxt=curr.next
                curr.next=nxt.next
                nxt.next=grp_prev.next
                grp_prev.next=nxt
            
            grp_prev=curr
        
        return dummy.next
    
    def getKth(self,node,k):
        while node and k>0:
            node=node.next
            k-=1
        return node



