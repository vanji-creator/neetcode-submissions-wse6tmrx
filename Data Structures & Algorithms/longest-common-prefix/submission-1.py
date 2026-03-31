class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        maxLen=len(strs[0])
        for i in strs:
            if i == "":
                return ""
            if maxLen>len(i):
                maxLen=len(i)

        lcp=[]
        i=0

        while i < maxLen:
            currentChar = strs[0][i]
            for string in strs:
                if currentChar != string[i]:
                    return "".join(lcp)
                
            lcp.append(string[i])
            i+=1
        
        return "".join(lcp)

        



        