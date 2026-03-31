class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
        self.freq=1

class DoublyLinkedList:
    def __init__(self):
        self.head=Node(0,0)
        self.tail=Node(0,0)

        self.head.next=self.tail
        self.tail.prev=self.head
        self.size=0

    def append(self,node):
        nxt=self.head.next
        node.next=nxt
        node.prev=self.head
        self.head.next=node
        nxt.prev=node
        self.size+=1
    def pop(self,node=None):
        if node==None:
            node=self.tail.prev
        
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
        self.size-=1
        return node
class LFUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.size=0
        self.node_map={}
        self.freq_map=collections.defaultdict(DoublyLinkedList)
        self.min_freq=1

    def _update(self,node):
        old_freq=node.freq
        self.freq_map[old_freq].pop(node)

        if self.min_freq==old_freq and self.freq_map[old_freq].size==0:
            self.min_freq+=1
        
        node.freq=old_freq+1
        self.freq_map[old_freq+1].append(node)


    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        
        node=self.node_map[key]
        self._update(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.node_map:
            node=self.node_map[key]
            self._update(node)
            self.node_map[key].val=value
        
        else:
            if self.cap==self.size:
                evicted=self.freq_map[self.min_freq].pop()
                del self.node_map[evicted.key]
                self.size-=1
            
            node=Node(key,value)
            self.freq_map[1].append(node)
            self.node_map[key]=node
            self.min_freq=1
            self.size+=1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)