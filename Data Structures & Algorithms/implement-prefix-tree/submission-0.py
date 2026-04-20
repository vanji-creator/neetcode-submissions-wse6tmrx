class TrieNode:
    
    def __init__(self):
        self.children={}
        self.isWord=False

class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        current=self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current=current.children[char]
        current.isWord=True


    def search(self, word: str) -> bool:
        current=self.root
        for char in word:
            if char not in current.children:
                return False
            current=current.children[char]
        if current.isWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        current=self.root
        for char in prefix:
            if char not in current.children:
                return False
            current=current.children[char]
        return True
        
        