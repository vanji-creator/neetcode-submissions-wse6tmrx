class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        tMap={}
        for left in range(len(t)):
            tMap[t[left]]=tMap.get(t[left],0)+1
        
        window={}
        res,res_len=[0,0],float("inf")
        have,need=0,len(tMap)

        left=0
        for right in range(len(s)):
            c=s[right]
            window[c]=window.get(c,0)+1

            if c in tMap and window[c]==tMap[c]:
                have+=1
            
            while have==need:

                if right-left+1<res_len:
                    res=[left,right]
                    res_len=right-left+1
                
                leftC=s[left]
                window[leftC]-=1

                if leftC in tMap and window[leftC]<tMap[leftC]:
                    have-=1
                
                left+=1
        
        if res_len==float("inf"):
            return ""
        
        left,right=res
        return s[left:right+1]







