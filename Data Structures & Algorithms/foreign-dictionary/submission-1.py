from collections import deque,defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        children={}
        inDeg={}

        for word in words:
            for ch in word:
                inDeg[ch]=0
                children[ch]=[]


        for i in range(len(words)-1):
            len1=len(words[i])
            len2=len(words[i+1])
            shorterLength=min(len1,len2)
            for j in range(shorterLength):
                if words[i][j]!=words[i+1][j]:
                    children[words[i][j]].append(words[i+1][j])
                    inDeg[words[i+1][j]]+=1
                    break
            else:
                if shorterLength!=len1:
                    return ""

        queue=deque()
        for char in children:
            if inDeg[char]==0:
                queue.append(char)

        order=[]
        while queue:
            letter=queue.popleft()
            order.append(letter)
            for dependent in children[letter]:
                inDeg[dependent]-=1
                if inDeg[dependent]==0:
                    queue.append(dependent)
        
        return "".join(order) if len(order)  == len(children) else ""