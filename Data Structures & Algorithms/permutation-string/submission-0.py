class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        LenS1=len(s1)
        window={}
        s1Map={}

        for k in range(LenS1):
            s1Map[s1[k]]=s1Map.get(s1[k],0)+1

        for right in range(len(s2)):
            window[s2[right]]=window.get(s2[right],0)+1
            while (right-left+1) == LenS1:
                if window==s1Map:
                    return True
                else:
                    if window[s2[left]]>1:
                        window[s2[left]]-=1
                    else:
                        del window[s2[left]]
                    left+=1
        return False
            