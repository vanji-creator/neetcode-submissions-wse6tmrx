class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        window={}
        max_freq=0
        result=0

        for right in range(len(s)):
            window[s[right]]=1+window.get(s[right],0)
            max_freq=max(window.values())

            while (right-left+1) -max_freq>k:
                window[s[left]]-=1
                left+=1

            result=max(result,right-left+1)
        
        return result