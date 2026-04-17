class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        results=[]
        backpack=[]
        wordSet=set(wordDict)

        def dfs(start):
            if start==len(s):
                results.append(" ".join(backpack))
                return
            
            for i in range(start,len(s)):
                if s[start:i+1] in wordSet:

                    backpack.append(s[start:i+1])
                    dfs(i+1)
                    backpack.pop()

        dfs(0)
        return results