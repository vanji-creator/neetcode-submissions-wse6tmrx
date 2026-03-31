from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        #goal is to arrange the string so that no adjacent char are same
        #store all chars in a set, take an element from the set
        #check if any element other than the current one is present in the set
        #if its there yes, and finally if set is empty return 
        #otherwise return empty string
        #but we have to try different orders before returning empty string
        #another approach in mind, use a dictionary first to find the frequency of
        #all the letters, try to place diff chars with most frequencies because
        #we have to complete most frequent ones first so that there arent more of
        #them like more than one at the end, then gradually reduce from frequent ones
        #to less frequent ones as the frequent ones get lesser and matches others
        #i feel like i can use a heap here to get the most frequent one always
        #once i place the most frequent one, then i have to use other than it, 
        #should i pop n times until i get a diff char and push the same chars again
        #to the heap
        
        counter = Counter(s)
        maxHeap=[(-freq,char) for char,freq in counter.items()]

        result=""
        prev=None

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            
            freq,currentChar=heapq.heappop(maxHeap)
            result+=currentChar

            if prev :
                heapq.heappush(maxHeap,prev)
                prev=None

            freq+=1
            if freq<0:
                prev=(freq,currentChar)
            
        return result


            
