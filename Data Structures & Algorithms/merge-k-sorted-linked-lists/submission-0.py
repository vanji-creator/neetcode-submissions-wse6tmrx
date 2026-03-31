# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap=[]

        dummy=ListNode()
        curr=dummy

        for i,l in enumerate(lists):
            if l:
                heapq.heappush(min_heap,(l.val,i,l))

        while min_heap:
            val,i,node=heapq.heappop(min_heap)
            curr.next=node
            curr=curr.next

            if node.next:
                heapq.heappush(min_heap,(node.next.val,i,node.next))
            
        return dummy.next
            

            

            
        