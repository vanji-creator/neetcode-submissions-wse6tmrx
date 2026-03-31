class Node:

    def __init__(self,key,value):
        self.key=key
        self.value=value

        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.size=capacity
        self.cache={}

        self.left=Node(0,0)
        self.right=Node(0,0)

        self.left.next=self.right
        self.right.prev=self.left
        
    def insert(self,node):
        prevNode=self.left
        nextNode=self.left.next

        node.prev=prevNode
        node.next=nextNode

        prevNode.next=node
        nextNode.prev=node
    
    def remove(self,node):
        prevNode=node.prev
        nextNode=node.next

        prevNode.next=nextNode
        nextNode.prev=prevNode

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.size:
            lru=self.right.prev 
            self.remove(lru)
            del self.cache[lru.key]  
