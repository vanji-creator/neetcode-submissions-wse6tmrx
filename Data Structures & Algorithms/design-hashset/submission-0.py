class MyHashSet:

    def __init__(self):
        self.hashset=[]

    def add(self, key: int) -> None:
        condition=True
        for i in range(len(self.hashset)):
            if self.hashset[i]==key:
                condition=False
        if condition:
            self.hashset.append(key)
        

    def remove(self, key: int) -> None:
        k=0
        for i in range(len(self.hashset)):
            if self.hashset[i]!=key:
                self.hashset[k]=self.hashset[i]
                k+=1
        self.hashset[:]=self.hashset[0:k]

    def contains(self, key: int) -> bool:
        for i in range(len(self.hashset)):
            if self.hashset[i]==key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)