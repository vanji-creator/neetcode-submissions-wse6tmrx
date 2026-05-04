class TrieNode:

    def __init__(self):
        self.children={}
        self.isWord=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        current=self.root
        for char in word:
            if char not in current.children:
                current.children[char]=TrieNode()
            current=current.children[char]
        current.isWord=True
        

    def search(self, word: str) -> bool:
        def dfs(node,index):
            if index==len(word):
                return node.isWord
            
            char=word[index]
            if char !=".":
                if char in node.children:
                    return dfs(node.children[char],index+1)
                else:
                    return False
            
            for char in node.children.values():
                if dfs(char,index+1):
                    return True
            return False
        

        return dfs(self.root,0)
