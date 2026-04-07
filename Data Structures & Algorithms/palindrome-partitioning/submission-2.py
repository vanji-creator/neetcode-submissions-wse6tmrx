class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer=[]
        backpack=[]
        
        def isPalindrome(word):
            i=0
            j=len(word)-1

            while i<=j:
                if word[i]!=word[j]:
                    return False
                i+=1
                j-=1
            return True
        

        def dfs(i,current):
            #2 choices, include current one in the string or cut of string and 
            # add current one in a separate string
            if i>=len(s):
                if isPalindrome(current):
                    backpack.append(current)
                    answer.append(backpack[:])
                    backpack.pop()
                return
            
            #choice 1, continue forming the string
            dfs(i+1,current+s[i])

            #choice 2, cut off here, start new string

            if isPalindrome(current):
                backpack.append(current)
                dfs(i+1,s[i])
                backpack.pop()
            
        
        dfs(1,s[0])
        return answer
            


