class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        s=[]
        while i<len(word1) and i<len(word2):
            s.append(word1[i])
            s.append(word2[i])
            i+=1
        if len(word1)>len(word2):
            s.append(word1[i:])
        else:
            s.append(word2[i:])
        return "".join(s)


        