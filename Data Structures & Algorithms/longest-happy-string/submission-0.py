class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #it requires longest possible string, so must use all the occurences of 3 if possible
        #if the cooldown window does not allow all the occurence, only then shrink
        #use a heap to keep key value pairs of a,b,c
        #reduce freq as it gets used
        #maintain cooldown window or prev if we use a or b or c more than twice
        #once cooldown over try to use it if heap still has elements
        #else no
        maxHeap=[]
        if a>0:
            maxHeap.append((-a,"a"))
        if b>0:
            maxHeap.append((-b,"b"))
        if c>0:
            maxHeap.append((-c,"c"))
        heapq.heapify(maxHeap)
        resultString=""

        while maxHeap:
            freq,char=heapq.heappop(maxHeap)
            if len(resultString) >= 2 and resultString[len(resultString)-1]==char and resultString[len(resultString)-2] == char:
                tempChar,tempFreq=char,freq
                if maxHeap:
                    newFreq,newChar=heapq.heappop(maxHeap)
                    resultString+=newChar
                    newFreq+=1
                    if tempFreq<0:
                        heapq.heappush(maxHeap,(tempFreq,tempChar))
                    if newFreq<0:
                        heapq.heappush(maxHeap,(newFreq,newChar))
                else:
                    return resultString
            else:
                resultString+=char
                freq+=1
                if freq<0:
                    heapq.heappush(maxHeap,(freq,char))
        return resultString
            
            
            