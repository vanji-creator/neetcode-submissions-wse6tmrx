class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        matchsticks.sort(reverse=True)
        total=0
        for stick in matchsticks:
            total+=stick
        
        if total%4!=0:
            return False

        target=total//4
        #four spots
        spots=[target]*4

        def dfs(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if (spots[j]-matchsticks[i])<0:
                    continue
                
                spots[j]-=matchsticks[i]
                if dfs(i+1)==True:
                    return True
                    
                spots[j]+=matchsticks[i]
            return False
            
        return dfs(0)
            


        